#!/usr/bin/env python3
import os
import tarfile

# os.chdir('/tmp')
# tar = tarfile.open('/tmp/passwd.gz', 'w:gz')
# tar.add('passwd')
# tar.close()

# os.chdir('/mnt')
# tar = tarfile.open('/tmp/passwd.gz', 'r:gz')
# tar.extractall()
# tar.close()
a = os.walk('/mnt')
print(a.__next__())
print(a.__next__())
