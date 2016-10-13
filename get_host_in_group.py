#!/usr/bin/python
# Script to get host in hostgroup
from pyzabbix import ZabbixAPI, ZabbixAPIException


ZABBIX_SERVER = 'http://127.0.0.1/zabbix/'
zapi = ZabbixAPI(ZABBIX_SERVER)

#AUTH
zapi.login('Admin','zabbix')

for h in zapi.host.get(output='extend',
                             groupids=1):
    print h['host']+';'+h['status']
    
