#!/usr/bin/python2.7
##SCRIPT to monitoring Facebook with Zabbix
import sys
import argparse
import urllib2
import json
# unread_message_count == Messenger not read
# fan_count == like in page
# comments.summary(total_count).limit(0)
# page_total_actions == Actions on Page
# page_views_total == Page Views


first_arg =  sys.argv[1] 
second_arg = sys.argv[2]
page_id = "<ID_YOUR_PAGE>" # any username or id
access_token = '<ACESS_TOKEN>' 
page_data = None
api_endpoint = "https://graph.facebook.com/"
def zbxmonitoringfields(fbfields):
    fb_graph_url = api_endpoint+page_id+"?fields="+fbfields+"&access_token="+access_token
    #fb_graph_url = api_endpoint+page_id+"/posts?fields="+fbfields+"&access_token="+access_token
    api_request = urllib2.Request(fb_graph_url)
    api_response = urllib2.urlopen(api_request)
    page_data = json.loads(api_response.read())
    print page_data.pop(fbfields)


def zbxmonpost(fbfields):
    fb_graph_url = api_endpoint+page_id+"/posts?fields=comments.summary("+fbfields+")&access_token="+access_token
    api_request = urllib2.Request(fb_graph_url)
    api_response = urllib2.urlopen(api_request)
    page_data = json.loads(api_response.read())
    Sum = 0 
    for i in page_data['data']:
        line = i['comments']['summary'].pop('total_count')
        if line > 0:
            Sum += line
    print Sum

def zbxfields( fbfields, *period ):
    period = sys.argv[3]
    fb_graph_url = api_endpoint+page_id+"/insights/"+fbfields+"?period="+period+"&access_token="+access_token
    api_request = urllib2.Request(fb_graph_url)
    api_response = urllib2.urlopen(api_request)
    page_data = json.loads(api_response.read())

    for i in page_data['data']:
        res = i['values'][1]['value']
        print res

if __name__ == '__main__':
   eval(first_arg+"('{0}')".format(second_arg)) 
