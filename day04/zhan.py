
zhai=[]
def yazhai(str):
    zhai.append(str)

def chuzhai():
    zhai.pop(-1)

def chazhai():
    print(zhai)
if __name__ == '__main__':
    while True:
        choice=input('''what do you want to do:
    1,yazhai
    2,chuzhai
    3,chazhai
    else to exit
    input 1/2/3
    ''' )
        if choice == '1':
            print('please input content,print "end" to back to the menu,print "exit" to exit')
            while True:
                content=input('> ')
                if content != 'end':
                    yazhai(content)
                else:
                    break
        if choice == '2':
            chuzhai()
        if choice == '3':
            chazhai()
        else:
            exit()


