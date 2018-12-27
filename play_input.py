import traceback

print('Program starts...')
n = input('Enter n : ')

'''ni = int(n)
print('Odd') if ni % 2 else print('Even')


print('Program ends.')'''

# python env -> play_input -> int('goood') -> ValueError -> play_input -> python env -> prints the error

# play_input handling the error (exception)
# python env -> play_input -> int('goood') -> ValueError -> play_input

try:
  ni = int(n)
except ValueError:
  traceback.print_exc()
else:
  # this block will execute when there are no errors thrown in the corresponding try block
  print('Odd') if ni % 2 else print('Even')

print('Program ends.')
