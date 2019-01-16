import random
import sys
import string

# box='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+'
# def getrandpass(long):
#     passwdbox = []
#     for i in range(long):
#         passwdbox.append(random.choice(box))
#     for i in range(len(passwdbox)):
#         print(passwdbox[i],end='')
#
# getrandpass(int(sys.argv[1]))

box2=string.ascii_letters+string.digits
def getrandpass2(long=8):
    result=''
    for i in range(long):
        letter=random.choice(box2)
        result += letter
    return result

if __name__ == '__main__':
    print(getrandpass2())