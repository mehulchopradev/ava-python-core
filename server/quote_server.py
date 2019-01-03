import socket
import time
from threading import Thread

class Serverthread(Thread):
  def __init__(self, cs):
    super().__init__()

    self.cs = cs

  def run(self):
    n = int(self.cs.recv(4096))
    
    q = quotes[n-1]
    time.sleep(30) # emulate a long running server service
    
    self.cs.send(q.encode('utf-8'))


quotes = ['Time tide waits for no man', 'bdfgg', 'Honesty is best', 'fefefefwefw']

ss = socket.socket()

port = 5700
backlog = 5

ss.bind(('', port))
ss.listen(2)

while True:
  print('Server started. Waiting for connection...')
  cs, address = ss.accept()
  print('Connection accepted from ' + str(address))

  thread = Serverthread(cs)
  thread.start()