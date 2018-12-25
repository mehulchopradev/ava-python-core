def perimeter(length, breadth=3):
  return 2 * (length + breadth)

def area(length, breadth):
  return length * breadth

l1 = float(input('Enter length: '))
b1 = float(input('Enter breadth: '))

p = perimeter(l1, b1)
a = area(l1, b1)

# p, a are global script level variables
# only refer their values inside the functions defined in the script
# can refer as well as change their values anywhere apart from function in the script

print(p)
print(a)

def abc():
  # global p # avoid this!
  p = 45
  # a variable is created in a scope (global or function) in python, whenever u give a value to the variable
  #  in python if-else, loops, classes or any other kind of non function blocks, never ever create own scopes
  # p will be created as a local variable to the function abc
  print(p) # works

abc()
print(p)