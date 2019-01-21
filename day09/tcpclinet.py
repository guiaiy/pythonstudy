import socket

server = '192.168.4.254'
port = 1234
addr = (server, port)
c = socket.socket()
c.connect(addr)
while True:
    data = input('> ') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break
    recv_data = c.recv(1024)
    print(recv_data)
c.close()
