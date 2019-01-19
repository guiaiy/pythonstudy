#!/usr/bin/env python3
import tkinter
from functools import partial


def hello():
    lb1.config(text='Hello China')


def welcom():
    lb1.config(text='Hello Tedu')


def say_hi(word):
    def greet():
        lb1.config(text='Hello %s' % word)

    return greet


root = tkinter.Tk()
lb1 = tkinter.Label(root, text='Hello World?', font='monofur 20 bold')
MyButton = partial(tkinter.Button, root, fg='white', bg='blue')

b1 = MyButton(text='Button 1', font='monofur 20 bold', command=hello)
b2 = MyButton(text='Button 2', font='monofur 20 bold', command=say_hi('Beijing'))
b3 = MyButton(text='Button 3', font='monofur 20 bold', command=say_hi('Tedu'))
b4 = MyButton(text='quit', font='monofur 20 bold', command=root.quit)

for item in (lb1, b1, b2, b3, b4):
    item.pack()

root.mainloop()
