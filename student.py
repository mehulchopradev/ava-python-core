# OOP
# Visualize a real world student in the software (allocating memory for every Student in the RAM) - Creating objects in the RAM
# Attributes of a Student (name, gender, roll, marks to be saved with every Student in the RAM)
# Call out actions on a Student (get_details, get_grade functions to be callable on every Student in the RAM)

# custom object - my own data type to the object - Student - class - gives data type to the objects created from it
# class is like a blueprint for the objects that will be created from it

class Student:
  def __init__(self, name=None, roll=None, gender=None, marks=None, contact_nos=None):
    # initialize the attributes in the object (s1 or s2 or s3 -> self)
    # constructor
    # parameterized contructor
    # overloaded constructors
    self.name = name
    self.roll = roll
    self.gender = gender
    self.marks = marks
    if contact_nos is None or isinstance(contact_nos, list):
      self.contact_nos = contact_nos
    else:
      print('Hey contact nos to be a list')

  def get_details(self):
    result = 'Name : ' + self.name + '\nGender: ' + self.gender + '\nRoll : ' + str(self.roll)\
       + '\nMarks : ' + str(self.marks) + '\n'

    if self.contact_nos is not None:
      for contact_no in self.contact_nos:
        result += contact_no + '\n'

    return result

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
  s1 = Student('mehul', 10, 'm', 90, nos)
  name, roll = s1.get_name_roll() # tuple unpacking
  print(name)
  print(roll)

  print(s1.get_details()) # Student.get_details(s1)
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