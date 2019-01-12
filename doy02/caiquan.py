import random
allchoice=['石头','剪刀','布']
winlist=[['石头','剪刀'],['剪刀','布'],['布','石头']]
print('请出拳：0，石头  1，剪刀  2，布   选择0/1/2')
numchoice=int(input())
humchoice=allchoice[numchoice]
comchoice=random.choice(allchoice)

if humchoice==comchoice:
    print('电脑：',comchoice,' , ','玩家：',humchoice)
    print('\033[32;1m打平了\033[0m')
elif [humchoice,comchoice] in winlist:
    print('电脑：', comchoice, ' , ', '玩家：', humchoice)
    print('\033[31;1m你赢了\033[0m')
else:
    print('电脑：', comchoice, ' , ', '玩家：', humchoice)
    print('\033[31;1m你输了\033[0m')




