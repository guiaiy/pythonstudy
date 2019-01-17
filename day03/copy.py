###将/bin/ls复制到/tmp/list
import sys

# with open('/bin/ls','rb') as f1:
#     with open('/tmp/list','wb')as f2:
#         data=f1.read(4096)
#         while data:
#             f2.write(data)
#             data=f1.read(4096)


def copy(src, dest):
    with open(src, 'rb') as f1:
        with open(dest, 'wb')as f2:
            data = f1.read(4096)
            while data:
                f2.write(data)
                data = f1.read(4096)


copy(sys.argv[1], sys.argv[2])