num=int(input('please input a number: '))

###
sum=0
def fei(n):
    if n==1 or n==2:
        return 1
    else:
        return fei(n-1)+fei(n-2)

for i in range(1,num):
    print(fei(i),end=', ')
print(fei(num))

###
f1,f2,f3=1,1,0
print(f1,f2,end=', ')
for i in range(num-2):
    f3=f2+f1
    print(f3,end=', ')
    f1=f2
    f2=f3

###
feilist = []

if num==1:
    feilist.append(1)
elif num==2:
    feilist.append(1)
    feilist.append(1)
else:
    feilist.append(1)
    feilist.append(1)
    for i in range(2,num):
        feilist.append(feilist[-1]+feilist[-2])

print(feilist)

