import socket

host = ''
port = 1234
addr = (host, port)
s = socket.socket()
s.bind(addr)
s.listen(1)
cli_sock, cli_addr = s.accept()
data = cli_sock.recv(1024)
print(data)
cli_sock.send(b'Hello\r\n')
cli_sock.close()
s.close()
