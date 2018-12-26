from address import Address

class Author:
  def __init__(self, name, gender, ratings, address=None):
    self.name = name
    self.gender = gender
    self.ratings = ratings

    if isinstance(address, Address):
      # composition association
      # where the Address obj exists in the system only till the Author obj exists
      self.address = address
    else:
      self.address = None

  def get_details(self):
    part1 = 'Name : {0}\nGender : {1}\nRatings: {2}\n'.format(self.name, self.gender, self.ratings)
    if self.address is not None:
      part2 = self.address.get_details()
    else:
      part2 = 'Address : NA'

    return part1 + part2

if __name__ == '__main__':
  addr1 = Address('India', 'MH', 'Mumbai', '400053')
  a1 = Author('mehul', 'm', 5, addr1)

  a2 = Author('jane', 'f', 4)

  print(a1.get_details())
  print(a2.get_details())