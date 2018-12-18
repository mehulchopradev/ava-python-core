def perimeter(length, breadth):
  return 2 * (length + breadth)

def area(length, breadth):
  return length * breadth

l1 = float(input('Enter length: '))
b1 = float(input('Enter breadth: '))

p = perimeter(l1, b1)
a = area(l1, b1)

print(p)
print(a)