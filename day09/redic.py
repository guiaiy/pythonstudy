#!/usr/bin/env python3
import re
from collections import Counter
c = Counter()
c.update(['192.168.1.1'])
c.update(['192.168.1.2'])
c.update(['192.168.1.3', '192.168.1.3', '192.168.1.4', '192.168.1.2', '192.168.1.4', '192.168.1.3'])
print(c)
print(c.most_common(3))

dic = {}


print(Counter('12333'))