from college_user import CollegeUser

class PhotoSession:

  @staticmethod
  def takephoto(user):
    if isinstance(user, CollegeUser):
      print('Photo taken of {0}'.format(user.name))
    else:
      print('Hey pass in a Student')