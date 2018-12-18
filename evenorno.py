n = int(input('enter n : '))

# this is a traditional python if-else
'''if n % 2:
  print('It is odd')
else:
  print('It is even')'''

# pre condition
# both the if and else branch should have only one instruction
# if comprehensions
print('It is odd') if n % 2 else print('It is even')