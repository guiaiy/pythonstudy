import requests
import json


url = 'http://139.159.248.149:3680/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
# 96a83c3078ef822048bbe48123577936