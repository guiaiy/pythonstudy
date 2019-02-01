import json
from pprint import pprint

import requests

url = 'http://139.159.248.149:3680/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.get",
#     "params": {
#         "output": "extend"
#     },
#     "auth": "96a83c3078ef822048bbe48123577936",
#     "id": 1
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "96a83c3078ef822048bbe48123577936",
#     "id": 1
# }
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "webserver1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.1.3",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "96a83c3078ef822048bbe48123577936",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
pprint(r.json())
