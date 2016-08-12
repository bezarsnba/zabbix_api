#!/usr/bin/python
# -*- coding: utf-8 -*-
# Script para desabilitar ações
# statusAction= 1(Disabled) 0 (enabled)
# Autor: Bezaleel Ramos da Silva
#

from zabbixAPI import zapi
from sys import argv
auth = zapi( '', 'user.login', '' )

statusAction=argv[1]

def updateAction(idAction,statusAction):
        updateAction = {
              "actionid":idAction,
              "status":statusAction,
        }
        ##Atualizar action .
        update = zapi( updateAction, 'action.update', auth )
        return update

if __name__ == '__main__':
        updateAction('26',statusAction)
        updateAction('23',statusAction)
