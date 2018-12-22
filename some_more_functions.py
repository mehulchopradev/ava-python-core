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

  return mno

a = pqr()
# a will be having an address of the mno function
print(a())