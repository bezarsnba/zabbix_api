from pyzabbix import ZabbixAPI, ZabbixAPIException

#URL
ZABBIX_SERVER = 'http://127.0.0.1/zabbix/'
zapi = ZabbixAPI(ZABBIX_SERVER)

#AUTH
zapi.login('Admin','zabbix')

ArqHost = open("/home/dir.txt", 'r').read().split('\n')
'''
    File dir.txt contain the parameters
    Column 1: Host
'''
def addTemplateHost():
    for linha in ArqHost:
     zHost = linha.split(';')  
     getHostId = zapi.host.get(filter={"host": zHost[0].lower()},
                                output=["hostid"])
     addTemplate = zapi.template.massadd(hosts= getHostId[0]['hostid'],
                                        templates={"templateid":'16999'})

     print  "Adding Template in Host: %s" % zHost[0]

if __name__ == '__main__':
addTemplateHost()
