#!/usr/bin/env python3
import time
from datetime import datetime,timedelta

t = time.time()
print(t)

t = time.localtime()
print(t)

# time.sleep(1)

t = t.tm_year
print(t)

t = time.strftime('%Y-%m-%d %H:%M:%S %a %A')
print(t)

t = datetime.now()
print(t)

a = t.year
print(a)

days = timedelta(days = 60)

a = t - days
print(a)

a = t + days
print(a)
print(a.month)
print(a.day)