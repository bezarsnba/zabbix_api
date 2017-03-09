from pyzabbix import ZabbixAPI, ZabbixAPIException
import time
 
#URL
ZABBIX_SERVER = 'http://127.0.0.1/zabbix/'
zapi = ZabbixAPI(ZABBIX_SERVER)
 
#AUTH
zapi.login('Admin','zabbix')
 
period= 86400 * 29  # Um dia em segundos * 29 dias
startTime= int(time.time())
endTime= startTime- period
 
 
#Buscar o serviceID
def zbxGetSlaOnly(listaServicos):
        ZbxItSla = zapi.service.getsla(serviceids = listaServicos,
                                intervals ={
                                "from" :startTime,
                                "to" : endTime})
        slaOnly = [ i['sla'] for i in ZbxItSla[listaServicos]['sla']]
        return slaOnly
 
zbxItServices = zapi.service.get({"filter":"serviceid",
                                  "search":"root"})
for x in zbxItServices:
        print zbxGetSlaOnly(x['serviceid'])
