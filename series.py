# series.py is a module
# name of the module is 'series'

def fibo_series(n):
  result = ''
  a, b = 0, 1
  result = result + str(a) + '\t' + str(b) + '\t'

  for i in range(1, n-1):
    c = a + b
    result = result + str(c) + '\t'
    a, b = b, c

  return result

def even_series(n):
  result = ''
  for i in range(0, n + 1, 2): # range has 3rd argument called as step size
    result = result + str(i) + '\t'
  return result

# print(__name__) # evry python module has this variale available and already defined

if __name__ == '__main__':
  # module testing code
  n = int(input('hey enter n : '))
  print(fibo_series(n))