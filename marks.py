'''
 >= 70 - A
 >= 60 - B
 >= 40 - C
 < 40 - F
 > 100 or < 0 - I
 '''

marks = float(input('enter marks: '))
# scope of grade is going to be global (entire file)
if marks > 100 or marks < 0:
  grade = 'I'
elif marks >= 70:
  grade = 'A'
elif marks >= 60:
  grade = 'B'
elif marks >= 40:
  grade = 'C'
else:
  grade = 'F'

print(grade)