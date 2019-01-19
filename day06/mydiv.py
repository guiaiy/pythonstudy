#!/usr/bin/env python3


try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError):
    print('Invalid input.')
except (KeyboardInterrupt, EOFError):
    print('\nend')
else:  ##不发生异常才会执行
    print(result)
finally:  ##不管是否发生异常都会执行
    print('done')
