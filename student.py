# OOP
# Visualize a real world student in the software (allocating memory for every Student in the RAM) - Creating objects in the RAM
# Attributes of a Student (name, gender, roll, marks to be saved with every Student in the RAM)
# Call out actions on a Student (get_details, get_grade functions to be callable on every Student in the RAM)

# custom object - my own data type to the object - Student - class - gives data type to the objects created from it
# class is like a blueprint for the objects that will be created from it
from college_user import CollegeUser

class Student(CollegeUser):
  def __init__(self, name=None, roll=None, gender=None, marks=None, contact_nos=None):
    # initialize the attributes in the object (s1 or s2 or s3 -> self)
    # constructor
    # parameterized contructor
    # overloaded constructors

    super().__init__(name, gender, contact_nos)
    # self <- 4001
    # CollegeUser.__init__(self, name, gender, contact_nos)

    self.roll = roll
    self.marks = marks

  # method overriding
  def get_details(self):
    part1 = super().get_details()
    part2 = '\nRoll : {0}\nMarks : {1}'.format(self.roll, self.marks)
    return part1 + part2

  def get_grade(self):
    marks = self.marks
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

    return grade

  def get_name_roll(self):
    return (self.name, self.roll)

if __name__ == '__main__':
  nos = ['978857435', '873483248']
  # 4001
  s1 = Student('mehul', 10, 'm', 90, nos)
  # Student.__init__(4001, 'mehul', 10, 'm', 90, nos)
  name, roll = s1.get_name_roll() # tuple unpacking
  print(name)
  print(roll)

  print(s1.get_details()) # Student.get_details(s1) <- 4001
  # Reserve a random address in the RAM - 2002
  # s1 = Student.__init__(2002, 'mehul', 10, 'm', 90)
  # print(s1.name) # NA
  # print(s1.roll) # 0


  '''s1.name = 'mehul'
  s1.roll = 10
  s1.gender = 'm'
  s1.marks = 90'''

  s2 = Student('jane', 12, 'f', 80)
  print(s2.get_details()) # Student.get_details(s2)
  # Reserve a random address in the RAM - 2005
  # s2 = Student.__init__(2005, 'jane', 12, 'f', 80)

  '''s2.name = 'jane'
  s2.roll = 12
  s2.gender = 'f'
  s2.marks = 80'''

  # print(id(s1))
  # print(id(s2))

  print(s1 is s2) # False

  print(s1.get_grade()) # Student.get_grade(s1)
  print(s2.get_grade()) # Student.get_grade(s2)

  '''print(s1.name)
  print(s1.roll)

  print(s2.name)
  print(s2.roll)'''

  # bad
  my_nos = ['4464565435']
  s3 = Student(name='jill', gender='f', marks=100, roll=13, contact_nos=my_nos)
  s3.s_name = 'jill'
  s3.r = 13
  s3.gender = 'f'
  s3.total_marks = 100

  # print(s3.name)
  # print(s3.roll)

  print(s3.get_details())

  s4 = Student()
  # Student.__init__(3001)

  s5 = Student(name='mark', gender='m')