adict = {'name': 'bob', 'age': 22}
cdict = dict()
ddict = dict(['ab', ('name', 'alice'), ['age', 18]])
edict = {}.fromkeys(['tom', 'jerry'], 10)

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

# adict.pop('age')
# print(adict)

# fdict = adict
# print('%s : %s' % (id(fdict),id(adict)))
# fdict = adict.copy()
# print('%s : %s' % (id(fdict),id(adict)))

# print(adict['age'])
# print(adict.get('age'))  ###重要方法
# print(adict.get('ager'))
# print(adict.get('ager','not found'))
# # print(adict['ager'])

# adict.setdefault('name','tom') ##name已经存在，不会改变它的值
# adict.setdefault('email','123@321')
# print(adict)

adict.update({'email': '321@321'})
print(adict)
