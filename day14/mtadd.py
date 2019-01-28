import threading
import time


def add(n=40000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)


if __name__ == '__main__':
    start = time.time()
    tlist = []
    for i in range(2):
        t = threading.Thread(target=add)
        tlist.append(t)
        t.start()
    tlist[0].join()
    tlist[1].join()
    end = time.time()
    print(end - start)
