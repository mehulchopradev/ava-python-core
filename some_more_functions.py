def abc():
  x = 5 # local to abc

  # functions are treated as regular values like the x above (first class citizens)
  # local to abc
  def xyz():
    x = 10 # local to xyz 
    print(x) # the inner function can access the variables of its enclosing function # 10
    return 'xyz'

  print(x) # 5
  print(xyz()) # 'xyz'
  print(x) # 5


# abc()
# xyz() # this will not work

def pqr():
  x = 5
  # local to pqr

  # mno <- 3002 (function)
  def mno():
    return 'mno'

  # mno is a callable variable -> mno()
  # whereas x is not callable -> x() (wrong) -> print(x) (right)

  return mno # returning the address that mno is storing

a = pqr()
# a is a callable variable
# a will be having an address of the mno function
print(a())

def fun(f):
  # f is a local variable
  # f is a callable variable
  print('Fun')
  f()

def foo():
  print('Foo')

fun(foo)
# a function address can be passed as an argument to another function














