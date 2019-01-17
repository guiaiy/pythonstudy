#!/usr/bin/env python3

def menu(menu,choicelist):
    while True:
        select = input(menu).strip()
        if not select:
            print('你没有输入任何内容，')
            continue
        select = select[0]
        if select not in choicelist:
            print('输入超出范围，请重新输入')
            continue
        return select

if __name__ == '__main__':
    select = menu('''请选择
1
2
3
''', '123')
    print(select)