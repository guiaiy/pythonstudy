#!/usr/bin/env python3
import caiquan


def caiquan2():
    humwin = 0
    comwin = 0
    number = input('请输入想要猜拳的盘数（必须是奇数）  ')
    while not number.isdigit() or int(number) % 2 == 0 or int(number) < 0:
        print('输入有误，请重新输入')
        number = input('请输入想要猜拳的盘数（必须是奇数）  ')
    else:
        while humwin <= int(number) // 2 and comwin <= int(number) // 2:
            result = caiquan.caiquan()
            if result == 'win':
                humwin += 1
            elif result == 'lose':
                comwin += 1
        if humwin > comwin:
            print()
            print('\33[35;1m恭喜你，你获得了最终的胜利\33[0m')
            return 'humwins'
        else:
            print()
            print('\33[35;1m你输了，请再接再厉\33[0m')
            return 'comwins'


if __name__ == '__main__':
    caiquan2()
