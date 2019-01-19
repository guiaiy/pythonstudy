#!/usr/bin/env python3
import random


def caiquan():
    allchoice = ["石头", "剪刀", "布".center(3)]
    wins = [['石头', '剪刀'], ['剪刀', '布'.center(3)], ['布'.center(3), '石头']]
    comchoice = random.choice(allchoice)
    select = input('请选择  1:石头， 2:剪刀， 3:布  ')
    while select not in ['1', '2', '3']:
        print('输入有误，请重新选择')
        select = input('请选择  1:石头， 2:剪刀， 3:布  ')
    else:
        humchoice = allchoice[int(select) - 1]
        if humchoice == comchoice:
            print('电脑:\033[041;1m%s\033[0m vs 玩家:\033[041;1m%s\033[0m result:\033[031;1m平局\033[0m' % (
                comchoice, humchoice))
            return 'draw'
        if [humchoice, comchoice] in wins:
            print('电脑:\033[041;1m%s\033[0m vs 玩家:\033[041;1m%s\033[0m result:\033[031;1m你赢了\033[0m' % (
                comchoice, humchoice))
            return 'win'
        else:
            print('电脑:\033[041;1m%s\033[0m vs 玩家:\033[041;1m%s\033[0m result:\033[031;1m你输了\033[0m' % (
                comchoice, humchoice))
            return 'lose'


if __name__ == '__main__':
    caiquan()
