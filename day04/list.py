alist = [1, 2, 3, 4, [1, 2, 3]]
alist[-1] = 5
print(alist)
alist[1:3] = alist[3:1:-1]
print(alist)
alist[1:1] = [20, 30, 40]
print(alist)
print(alist.index(40))
alist.insert(alist.index(40) + 1, 80)
print(alist)
alist.pop(4)
print(alist)
alist.remove(4)
print(alist)
alist.reverse()
print(alist)
alist.sort()
print(alist)
alist.extend([1, 2])
print(alist)
blist = alist
print(alist)
blist.reverse()
print(alist)
clist = alist.copy()
print(clist)
