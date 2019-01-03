import socket


n = int(input('Enter n (1-4) : '))

cs = socket.socket()
cs.connect(('localhost', 5700))
cs.send(str(n).encode('utf-8'))

result = cs.recv(4096)
print(result)

cs.close()