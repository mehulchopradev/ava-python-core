from college_user import CollegeUser
class Professor(CollegeUser):
  def __init__(self, name, gender, subjects, contact_nos=None):
    super().__init__(name, gender, contact_nos)

    if isinstance(subjects, list):
      all_subjects = [subject for subject in subjects if isinstance(subject, str)]
      if len(all_subjects) == len(subjects):
        self.subjects = subjects
      else:
        # would rather raise an error from here
        self.subjects = None
    else:
      # would rather raise an error from here
      self.subjects = None

  # method overriding
  def get_details(self):
    part1 = super().get_details()
    part2 = self.get_subjects()
    return part1 + part2

  def get_subjects(self):
    result = ''
    if self.subjects is not None:
      for subject in self.subjects:
        result += subject + '\n'
    return result