import json

alist = [100, 200, 300]

jdata = json.dumps(alist)
print(jdata)
a = json.loads(jdata)
print(a)