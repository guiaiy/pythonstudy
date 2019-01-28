import os
import subprocess


def ping(host):
    rc = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
    if rc.returncode == 0:
        print('%s is up' % host)
    # else:
    #     print('%s is down' % host)


if __name__ == '__main__':
    ips = ('176.52.10.%s' % i for i in range(1, 254))
    for ip in ips:
        ret_val = os.fork()
        if not ret_val:
            ping(ip)
            exit()
