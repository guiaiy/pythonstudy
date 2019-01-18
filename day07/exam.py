#!/usr/bin/env python3
import random


# def add(x, y):
#     return x + y
#
#
# def sub(x, y):
#     return x - y


def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [random.randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    op = random.choice('+-')
    result = cmds[op](*nums)
    counter = 0
    while counter < 3:
        answer = int(input('%s %s %s = ? :  ' % (nums[0], op, nums[1])))
        if answer == result:
            print('\033[035;1mRight\033[0m')
            break
        print('\033[031;1mWrong\033[0m')
        counter += 1
    else:
        print('%s %s %s = %s' % (nums[0], op, nums[1], result))


def main():
    while True:
        exam()
        try:
            yn = input('Continue(y/n)?  ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'nN':
            print('\nBye-bye')
            break


if __name__ == '__main__':
    main()
