import random
import sys

box = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+'


def getrandpass(long):
    passwdbox = []
    for i in range(long):
        passwdbox.append(random.choice(box))
    for i in range(len(passwdbox)):
        print(passwdbox[i], end='')


getrandpass(int(sys.argv[1]))
