class CollegeUser:
  # self <- 4001
  def __init__(self, name, gender, contact_nos):
    self.name = name
    self.gender = gender

    if contact_nos is None or isinstance(contact_nos, list):
      self.contact_nos = contact_nos
    else:
      self.contact_nos = None

  def get_details(self):
    part1 = 'Name : {0}\nGender : {1}\n'.format(self.name, self.gender)
    part2 = ''
    if self.contact_nos is not None:
      for contact_no in self.contact_nos:
        part2 += contact_no + '\n'

    return part1 + part2