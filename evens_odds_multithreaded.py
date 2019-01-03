from threading import Thread, current_thread
import time

n = int(input('Enter n : '))

def printeven(n):
  t1 = current_thread()
  print(t1.getName() + ' has started execution')

  for i in range(0, n + 1, 2):
    print(i)
    time.sleep(3) # deliberate delay to emulate long running thread

def printodd(n):
  t2 = current_thread()
  print(t2.getName() + ' has started execution')

  for i in range(1, n + 1, 2):
    print(i)
    time.sleep(3) # deliberate delay to emulate long running thread

# main thread
main = current_thread()
print(main)
print(type(main))
print(main.getName())

t1 = Thread(target=printeven, args=(n,), name='EvenThread')
t2 = Thread(target=printodd, args=(n,), name='OddThread')

print(main.daemon)
print(t1.daemon)
print(t2.daemon)

t1.daemon = True
t2.daemon = True

# a python process will not terminate unless all non daemon threads have finished with their execution

t1.start()
t2.start()

'''t1.join()
t2.join()'''

print('Main thread done with execution')