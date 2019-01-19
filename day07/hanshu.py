# 参数


def set_age(name, age):
    print('%s is %s years old' % (name, age))


# 多个参数


def myfunc(*args):  ##  * 表示args是一个元组
    print(args)


def myfunc2(**kwargs):  ## **
    print(kwargs)


def add(x, y):
    print(x + y)


if __name__ == '__main__':
    myfunc()
    myfunc('hello')
    myfunc('hello', 123)

if __name__ == '__main__':
    set_age('bob', 23)
    set_age(age=23, name='bob')

if __name__ == '__main__':
    myfunc2()
    myfunc2(name='bob', age=23)

if __name__ == '__main__':
    add(10, 20)
    nums = [10, 20]
    add(nums[0], nums[1])
    add(*nums)
