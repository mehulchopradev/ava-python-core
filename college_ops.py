from student import Student
from professor import Professor
from photosession import PhotoSession

nos = ['978857435', '873483248']
# 4001
s1 = Student('mehul', 10, 'm', 90, nos)

p1 = Professor('mark', 'm', ['Physics', 'Chemistry'])

print(s1.get_details())
print(p1.get_details())

# print(p1.get_subjects())

PhotoSession.takephoto(s1)
PhotoSession.takephoto(p1)