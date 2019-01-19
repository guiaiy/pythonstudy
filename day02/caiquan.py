import random

humwin, comwin, count = 0, 0, 0
allchoice = ['石头', '剪刀', '布']
winlist = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
while humwin < 2 and comwin < 2 and count < 3:
    comchoice = random.choice(allchoice)
    numchoice = int(input('请出拳：0，石头  1，剪刀  2，布   选择0/1/2'))
    humchoice = allchoice[numchoice]
    if humchoice == comchoice:
        print('电脑：', comchoice, ' , ', '玩家：', humchoice)
        count += 1
        print('\033[32;1m打平了\033[0m')
        print()
    elif [humchoice, comchoice] in winlist:
        print('电脑：', comchoice, ' , ', '玩家：', humchoice)
        count += 1
        humwin += 1
        print('\033[31;1m你赢了\033[0m')
        print()
    else:
        print('电脑：', comchoice, ' , ', '玩家：', humchoice)
        count += 1
        comwin += 1
        print('\033[31;1m你输了\033[0m')
        print()
if humwin > comwin:
    print('最终胜利者是玩家')
elif comwin > humwin:
    print('最终胜利者是电脑')
else:
    print('双方打平')
