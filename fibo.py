# n = 8
# 0 1 1 2 3 5 8 13

n = int(input('enter n: '))

a, b = 0, 1

print(a)
print(b)

# for loop
# sequence of elements
# 1 to 6
# range(1 to n-1)

for i in range(1, n-1):
  c = a + b
  print(c)

  a, b = b, c
  '''
  a = b
  b = c
  '''