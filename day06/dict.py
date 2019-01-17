adict = {}
adict = {'name':'bob','age':22}
cdict = dict()
ddict = dict(['ab',('name','alice'),['age',18]])
edict = {}.fromkeys(['tom','jerry'],10)

# print('%s\n%s\n%s' % (adict,ddict,edict))
#
# for key in ddict:
#     print('%s : %s' % (key,ddict[key]))
#
# print('%(name)s : %(age)s' % ddict)
#
# for key,val in ddict.items():
#     print('%s : %s' % (key,val))
#
# for key in ddict.keys():
#     print(key)
#
# for val in ddict.values():
#     print(val)

# adict['age'] = 25
# adict['email'] = 'abc@qq.com'
# print(adict)

adict.pop('age')
print(adict)
