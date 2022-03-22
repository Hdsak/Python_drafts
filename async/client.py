import socket

sock = socket.socket()
sock.connect(('localhost', 5001))
sock.send('hello, world!'.encode())

data = sock.recv(1024)
print(data)