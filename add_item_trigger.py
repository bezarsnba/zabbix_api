
from pyzabbix import ZabbixAPI, ZabbixAPIException
### Simple script to create item/trigger in lote at Zabbix
### Parameter in file criaritem.txt:
###
### Ex: script.sh[Function,{HOST.IP},{HOST.NAME,000]

#URL
ZABBIX_SERVER = 'http://localhost/zabbix/'
zapi = ZabbixAPI(ZABBIX_SERVER)

#AUTH
zapi.login('Admin','zabbix')

ArqHost = open("C:\criaritem.txt", 'r').read().split('\n')

def criaItem():
    for linha in ArqHost:
        zSm = linha.split(',')
    if linha:
            item=zapi.item.create(
            hostid = "10000",
            name = "Name item %s" % zSm[2],
            key_= linha,
            type = 10,
            interfaceid = 615,
            delay =600,
            value_type = 2,
            history = 7,
            status=0,
            )

        continue

def criaTrigger():
    for linha in ArqHost:
        zItemHost = linha.split(',')
        ZCreateTrigger= zapi.trigger.create(
        host='10000',
        description="Name Item %s " % ( zItemHost[2]), 
        status=0,
        type=0,
        priority=2,
            expression='{Zabbix server:script.sh[Function,{HOST.IP},{HOST.NAME},000].str("ERROR")}=1' % zItemHost[2]
            )

criaItem()
