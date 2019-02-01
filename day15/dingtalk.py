import json

import requests

if __name__ == '__main__':
    url = 'https://oapi.dingtalk.com/robot/send?access_token=dc4d9876452e3d92bd80b36c73469ea51aafb487a7a49468e58e453fe813cf07'
    header = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "我就是我,  @13823550316 是不一样的烟火"
        },
        "at": {
            "atMobiles": [
                "13823550316"
            ],
            "isAtAll": False
        }
    }
    r = requests.post(url, headers=header, data=json.dumps(data))
    print(r.text)
