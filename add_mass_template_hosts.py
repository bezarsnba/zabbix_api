#!/usr/bin/python2.7
from pyzabbix import ZabbixAPI, ZabbixAPIException

#url
zbx_srv= 'https://localhost'
zapi = ZabbixAPI(zbx_srv)

#auth
zapi.login('admin','admin')

def addTemplateHost():
  getTemHostid = zapi.template.get(output=["hostid"],
                                      filter={'host': 'Template OS Windows'},
                                      selectHosts='hostid')
  
  for hostId in getTempHostid[0]['hosts']:
    addTemplate = zapi.template.massadd(hosts= linha['hostid'],
                                    templates=[{"templateid": '<templateids>'},
                                              {"templateid": '<templateids>'},
                                              {"templateid": '<templateids>'}])

    print "Add templates in hostsids %s" % hostId['hostid'] 

if __name__ == '__main__':
    
    addTemplateHost()