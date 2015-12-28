#!/bin/env python
import requests
import json
import sys

ZABIX_ROOT = 'https://hostname.com/zabbix'
ZABIX_URL = ZABIX_ROOT + '/api_jsonrpc.php'
ZABIX_USER = 'User.Api'
ZABIX_PASSWORD = 'Api'

GROUP = sys.argv[1]

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
# hostgroup.get
########################################
payload = {
    "jsonrpc" : "2.0",
    "method" : "hostgroup.get",
    "params": {
      'output': [
          'groupid',
          'name'],
       'filter': {
            'name': [
                GROUP,
            ]
        },
    },
    "auth" : res0['result'],
    "id" : 1,
}
res1 = requests.post(ZABIX_URL, data=json.dumps(payload), headers=headers, verify=False)
res1 = res1.json()
print 'We create maintenance for group:'
print(res1['result'][0]['groupid'])
########################################
# maintenance.create
########################################
payload = {
    "jsonrpc": "2.0",
    "method": "maintenance.create",
    "params": {
        "name": "Sunday maintenance",
        "active_since": 1358844540,
        "active_till": 1390466940,
        "groupids": [
            res1['result'][0]['groupid'],
        ],
        "timeperiods": [
            {
                "timeperiod_type": 3,
                "every": 1,
                "dayofweek": 64,
                "start_time": 64800,
                "period": 3600
            }
        ]
    },
    "auth": res0['result'],
    "id": 2
}
res2 = requests.post(ZABIX_URL, data=json.dumps(payload), headers=headers, verify=False)
