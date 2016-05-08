from pyzabbix import ZabbixAPI, ZabbixAPIException
import re

#URL
ZABBIX_SERVER = 'http://127.0.0.1/zabbix/'
zapi = ZabbixAPI(ZABBIX_SERVER)

#AUTH
zapi.login('Admin','zabbix')

ArqHost = open("C:\Users\p734790\Documents\Programas\dir.txt", 'r').read().split('\n')

'''
    File dir.txt contain the parameters
    Column 1: Host
    Column 2: Macro ID
    Column 3: Value
'''

def findMacroIDHostID():
    for linha in ArqHost:
     zHost = linha.split(';')
     getHostId = zapi.host.get(filter={"host": zHost[0].lower()},output=["hostid"])
     getMacroId = zapi.usermacro.get(output="extend",
                                       hostids = getHostId[0]['hostid'],
                                       filter={"macro":zHost[1]})
     hostMacroValue = getMacroId[0]['value'].split('/')[5].replace('_inter',';')+getMacroId[0]['macro'].replace('}','};')+getMacroId[0]['value']
     print hostMacroValue

def deleteMacro():
     for linha in ArqHost:
      zHost = linha.split(';')
      getHostId = zapi.host.get(filter={"host": zHost[0].lower()},output=["hostid"])
      getMacroId = zapi.usermacro.get(output="extend",
                                       hostids = getHostId[0]['hostid'],
                                       filter={"macro":zHost[1]})
      
      deleteMacroId = zapi.usermacro.delete(getMacroId[0]['hostmacroid'])
      print "Removed Macro: %s in Host: %s" % (zHost[1],zHost[0])

def addMacro():
    for linha in ArqHost:
     zHost = linha.split(';')  
     getHostId = zapi.host.get(filter={"host": zHost[0].lower()},
                                output=["hostid"])
     addMacro = zapi.usermacro.create(hostid= getHostId[0]['hostid'] ,
                                      macro= zHost[1],
                                       value= zHost[2])
     print "Adding Macro: %s in Host: %s" % (zHost[1],zHost[0])

	 
addMacro()