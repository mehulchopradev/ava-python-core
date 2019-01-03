import socket

cs = socket.socket()

cs.connect(('localhost', 5689))
data = cs.recv(4096)
print(data)

cs.close()