import os
import time

print('start...')
ret_val = os.fork()
if ret_val:
    print('in parent, sleep...')
    time.sleep(30)
    print('parent done')
else:
    print('in child, sleep...')
    time.sleep(10)
    print('child done')
