#!/usr/bin/env python3
stack = []

def show_menu():
    cmds = {'1':push,'2':pop,'3':view,}
    prompt = '''(1) push it
(2) pop it
(3) view it
(4) quit
please input your choice(1/2/3/4):  '''
    while True:
        choice = input(prompt).strip()
        if choice == '':
            print('Invalid input. Try again.')
            continue
        choice = choice[0]
        if choice not in '1234':
            print('Invalid input. Try again.')
            continue
        if choice == '4':
            return
        cmds[choice]()
        # if choice == '1':
        #     push()
        # if choice == '2':
        #     pop()
        # else:
        #     view()

def push():
    item = input('item to push: ').strip()
    if item:
        stack.append(item)

def pop():
    if stack:
        print('from stack popped %s' % stack.pop())

def view():
    print(stack)

if __name__ == '__main__':
    show_menu()