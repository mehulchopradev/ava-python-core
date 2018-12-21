from student import Student

nos = ['978857435', '873483248']
s1 = Student('mehul', 14, 'm', 90, nos)

s2 = Student('jane', 12, 'f', 80)

my_nos = ['4464565435']
s3 = Student(name='jill', gender='f', marks=100, roll=13, contact_nos=my_nos)

slist = [s1, s2, s3]

'''for student in slist:
  print(student.get_details())'''

# print('Scored more than 80 marks')

'''
for student in slist:
  if student.marks > 80:
    print(student.name)
'''

'''more_than_80 = [student.name for student in slist if student.marks > 80]
print(more_than_80)'''

roll = int(input('Enter roll : '))
for student in slist:
  if student.roll == roll:
    print(student.get_details())
    break


