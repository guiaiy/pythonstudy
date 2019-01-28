#!/usr/bin/env python3
import os
import socket
from time import strftime


class TcpTimeServer:
    def __init__(self, host='', port=1234):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
            cli_sock.send(data.encode())
            while True:
                result = os.waitpid(-1, 1)
                if result[0] == 0:
                    break

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            ret_val = os.fork()
            if not ret_val:
                self.serv.close()
                self.chat(cli_sock)
                cli_sock.close()
                exit()
            cli_sock.close()
        self.serv.close()


if __name__ == '__main__':
    tcp_serv = TcpTimeServer()
    tcp_serv.mainloop()
