import re

m = re.match('f..', 'food')
print(m.group())
print(re.search('^f..', 'seafood'))
m = re.search('f..', 'seafood')
print(m.group())
print(re.findall('f..', 'seafood is food'))
print(re.finditer('f..', 'seafood is food'))
for m in re.finditer('f..', 'seafood is food'):
    print(m.group(), end=' ')


m  = re.compile('f..')
print(m.findall('seafood'))
print()

print(re.split('-|\.', 'hello-world.tar.gz'))



print(re.sub('X', 'Mr.Smith', 'Hi X, Nice to meet you'))

print('abcddcdac.cad'.split(sep='a'))