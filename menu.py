'''
1. Print fibo series
2. Print even series
3. Print even or odd
4. Exit
Please enter ur choice : 1
Enter n: 8
0 1 1 2 3 5 8 13

1. Print fibo series
2. Print even series
3. Print even or odd
4. Exit
Please enter ur choice : 2
Enter n : 6
0 2 4 6

1. Print fibo series
2. Print even series
3. Print even or odd
4. Exit
Please enter ur choice : 3
Enter n : 5
Odd

1. Print fibo series
2. Print even series
3. Print even or odd
4. Print factorial
5. Exit
Please enter ur choice : 5
'''

# import series # importing the module
from series import fibo_series, even_series # directly importing functions from the module
# import com.abc.util.math
from com.abc.util.math import even_odd
from math import factorial

while True:
  print('1. Print Fibo Series\n2. Print even series\n3. Print even or odd\n4. Print factorial\n5. Exit')
  choice = int(input('Please enter ur choice: '))
  
  if choice != 5:
    n = int(input('Enter n : '))
    
  if choice == 1:
    print(fibo_series(n))
  elif choice == 2:
    print(even_series(n))
  elif choice == 3:
    print(even_odd(n))
  elif choice == 4:
    print(factorial(n))
  else:
    break # it forcibly breaks out of the surrounding loop
