import caiquan

def caiquan2():
    humwin = 0
    comwin = 0
    number = input('请输入想要猜拳的盘数（必须是奇数）  ')
    while int(number) % 2 == 0 or int(number) < 0:
        print('输入有误，请重新输入')
        number = input('请输入想要猜拳的盘数（必须是奇数）  ')
    else:
        while humwin <= int(number)//2 and comwin <= int(number)//2:
            result = caiquan.caiquan()
            if result == 'win':
                humwin += 1
            elif result == 'lose':
                comwin += 1
        if humwin > comwin:
            print('恭喜你，你获得了最终的胜利')
            return 'humwins'
        else:
            print('你输了，请再接再厉')
            return 'comwins'

if __name__ == '__main__':
    caiquan2()
