# accept variable number of arguments (parameters) 0 to n
# tuple packing
def myadd(*params):
  # print(params) # tuple
  s = 0
  for param in params:
    s += param
  return s

# positional arguments packing
print(myadd())
print(myadd(5))
print(myadd(4, 5, 3))
print(myadd(5, 6, 3, 4, 5, 1, 2))


# positional arguments unpacking
def perimeter(length, breadth):
  return 2 * (length + breadth)

stats = [6, 3] # cud even be a tuple
# print(perimeter(stats[0], stats[-1]))
print(perimeter(*stats)) # tuple/list unpacking

# dict packing
def area(**rectstats):
  # print(rectstats) # dict
  # {'l':5, 'b': 4}
  if 'length' in rectstats and 'breadth' in rectstats:
    return rectstats['length'] * rectstats['breadth']
  else:
    print('Hey pass in length and breadth keyword arguments')
    return 'NA'

# positional arguments
# block the end user from calling the function using positional arguments - Error
# print(area(5, 3))

# keyword arguments
# support calling functions only using keyword arguments

# keyword arguments packing
print(area(length=5, breadth=3))
print(area(breadth=3, length=5))
print(area(l=5, b=4))

# dict unpacking
statsmap = {'length': 9, 'breadth': 3}
# print(perimeter(statsmap['length'], statsmap['breadth']))
print(perimeter(**statsmap))

statsmap = {'breadth': 4, 'length': 10}
print(perimeter(**statsmap))