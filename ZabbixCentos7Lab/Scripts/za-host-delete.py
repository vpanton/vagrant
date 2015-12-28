#!/bin/env python
import requests
import json
import sys

ZABIX_ROOT = 'https://hostname.com/zabbix'
ZABIX_URL = ZABIX_ROOT + '/api_jsonrpc.php'
ZABIX_USER = 'User.Api'
ZABIX_PASSWORD = 'Api'

INSTANCE_HOSTNAME = sys.argv[1]

########################################
# user.login
########################################
payload = {
    "jsonrpc" : "2.0",
    "method" : "user.login",
    "params": {
      'user': ZABIX_USER,
      'password': ZABIX_PASSWORD,
    },
    "auth" : None,
    "id" : 0,
}
headers = {
    'content-type': 'application/json',
}
res0  = requests.post(ZABIX_URL, data=json.dumps(payload), headers=headers, verify=False)
res0 = res0.json()
########################################
# host.get
########################################
payload = {
    "jsonrpc" : "2.0",
    "method" : "host.get",
    "params": {
      'output': [
          'hostid',
          'name'],
       'filter': {
            'host': [
                INSTANCE_HOSTNAME,
            ]
        },
    },
    "auth" : res0['result'],
    "id" : 1,
}
res1 = requests.post(ZABIX_URL, data=json.dumps(payload), headers=headers, verify=False)
res1 = res1.json()
print 'We need delete host:'
print(res1['result'][0]['hostid'])
########################################
# host.delete
########################################
payload = {
    "jsonrpc" : "2.0",
    "method" : "host.delete",
    "params":[
        res1['result'][0]['hostid'],
    ],
    "auth" : res0['result'],
    "id" : 2,
}
res2 = requests.post(ZABIX_URL, data=json.dumps(payload), headers=headers, verify=False)
