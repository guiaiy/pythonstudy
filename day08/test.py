#!/usr/bin/env python3
import os
import time


def show_time(formats='%H:%M:%S'):
    pwd = os.getcwd()
    print(pwd)
    print(time.strftime(formats))


if __name__ == '__main__':
    show_time()
