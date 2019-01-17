#!/usr/bin/env python3
import string
import keyword
###合法返回0，空值返回1，keword返回2，首字符不合法返回3，其他字符不合法返回4,空值返回4###

def check_id(id):
    str = string.ascii_letters+'_'
    dig = string.digits
    if id == '':
        print('invalid:  \033[31;1m你什么都没有输入!\033[0m')
        return 1
    if id in keyword.kwlist:
        print('invalid:  \033[31;1m%s是一个关键字!\033[0m' % id)
        return 2
    if id[0] not in str:
        print('invalid:  \033[31;1m首位置必须是字母或者‘_’\033[0m')
        return 3
    for pos,otherletter in enumerate(id[1:]):
        if otherletter not in str+dig:
            print('invalid:  \033[31;1m第%s个字母"%s"不合法!\033[0m' % (pos+2,otherletter))
            return 4
    return 0


if __name__ == '__main__':
    check_id('')