# take a and b from the user (int) - Main thread
# 2 user defined threads
# 1 UDT should print addition of a and b
# 2nd UDT should print multiplication of a and b

from threading import Thread

class Additionthread(Thread):
  def __init__(self, a, b):
    super().__init__()

    self.a = a
    self.b = b

  def run(self):
    print(self.a + self.b)

class Multiplicationthread(Thread):
  def __init__(self, a, b):
    super().__init__()

    self.a = a
    self.b = b

  def run(self):
    print(self.a * self.b)

a = int(input('Enter a : '))
b = int(input('Enter b : '))

t1 = Additionthread(a, b)
t2 = Multiplicationthread(a, b)

t1.start()
t2.start()