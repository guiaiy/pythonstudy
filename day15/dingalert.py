#!/usr/bin/env python
import json
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "at": {
            "atMobiles": reminders,
            "isAtAll": False
        },
        "text": {
            "content": msg,
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return  r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = ['13823550316']
    url = 'https://oapi.dingtalk.com/robot/send?access_token=dc4d9876452e3d92bd80b36c73469ea51aafb487a7a49468e58e453fe813cf07'
    print(send_msg(url, reminders, msg))
