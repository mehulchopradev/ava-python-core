'''
 >= 70 - A
 >= 60 - B
 >= 40 - C
 < 40 - F
 > 100 or < 0 - I
 '''

marks = float(input('enter marks: '))
if marks > 100 or marks < 0:
  print('I')
elif marks >= 70:
  print('A')
elif marks >= 60:
  print('B')
elif marks >= 40:
  print('C')
else:
  print('F')