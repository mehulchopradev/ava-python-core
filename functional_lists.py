l = [5, 6, 3, 4, 2, 1, 9]

# filter (without for comprehensions)
# new list which has only the even elements from l

# callback function
'''def func(ele):
  return ele % 2 == 0'''

# lambda functions (expressions)
# functions with only one expression (statement)
# define the function at the line of passing it to another function (inline)

i = filter(lambda ele: ele % 2 == 0, l)
print(i)

# i is a sequence or an iterable on which we can loop. It is not some data structure like list
for e in i:
  print(e)

# mapping (without for comprehensions)
# new list which has squares of elements from l

# callback function
'''def squares(ele):
  return ele ** 2'''

i = map(lambda ele: ele ** 2, l)
for e in i:
  print(e)