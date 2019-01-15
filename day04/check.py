import keyword
import sys
import string

def check_id(word):
    id=string.ascii_letters+'_'
    other_id=string.ascii_letters+string.digits+'_'
    if word in keyword.kwlist:
        return 'invalid:  \033[31;1mThe letter %s is a passwd\033[0m' %(word)
    if word[0] not in id:
        return 'invalid:  \033[31;1mThe first position must be a letter or "_"'
    else:
        for ind,ch in enumerate(word[1:]):
            if ch not in other_id:
                return 'invalid:  \033[31;1mThe %sth letter "%s" is a invalid symbol\033[0m' % (ind+2,ch)
        return '\033[32;1mvalid\033[0m'

if __name__ == '__main__':
    result=check_id(sys.argv[1])
    print(result)