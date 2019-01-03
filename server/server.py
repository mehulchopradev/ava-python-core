import socket
from datetime import datetime

ss = socket.socket()

port = 5689
backlog = 5

ss.bind(('', port))
ss.listen(5)

while True:
  print('Server started. Waiting for connection...')
  cs, address = ss.accept()
  print('Connection accepted from ' + str(address))

  now = datetime.now()
  result = now.strftime('%d/%m/%Y %H:%M')

  cs.send(result.encode('utf-8'))