#!/usr/bin/env python3
class Vendor:
    def __init__(self, company, ph):
        self.company = company
        self.phone = ph

    def call(self):
        print('Calling %s...' % self.phone)


class PigToy:
    def __init__(self, name, color, company, ph):
        self.name = name
        self.color = color
        self.vendor = Vendor(company, ph)

    def show_me(self):
        print('Hi, my name is %s, I am %s' % (self.name, self.color))


class NewPigToy(PigToy):
    def walk(self):
        print('walking...')


piggy = PigToy('Piggy', 'pink', 'tedu', '400-800-1234')
piggy.show_me()
piggy.vendor.call()
# george = PigToy('George', 'red')
# george.show_me()
# print(piggy.name)

a = NewPigToy('Piggy', 'pink', 'tedu', '400-800-1234')
a.show_me()
a.vendor.call()
a.walk()
