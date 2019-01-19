import random

alist = [random.randint(1, 100) for i in range(10)]
print(len('hello'))

print(max(alist))
print(min(alist))

# print(enumerate(alist))
# print(list(enumerate(alist)))
for item in enumerate(alist):
    print('%s:%s' % item, end=' ')
print()

for ind, val in enumerate(alist):
    print('%s:%s' % (ind, val), end=' ')
print()

for ind2 in range(len(alist)):
    print('%s:%s' % (ind2, alist[ind2]), end=' ')
print()

print(reversed(alist))

for item2 in reversed(alist):
    print(item2, end=' ')
print()

print(sorted(alist))
