from author import Author
from address import Address

class Book:
  # attribute that is not there with every object
  # should be common to all objects
  __count = 0 # class attribute

  def __init__(self, title, price, pages, authors=None):
    # instance attributes (object attributes)
    self.title = title
    self.price = price
    self.pages = pages

    if authors is not None:
      if isinstance(authors, list):
        all_authors = [author for author in authors if isinstance(author, Author)]
        if len(all_authors) == len(authors):
          # aggregation association
          # on destroying the book obj from the system, the author obj in authors would not be destroyed
          self.authors = authors
        else:
          # would rather raise an error from here
          # self.authors = None
          raise ValueError('All authors need to be instance of Author class')
      else:
        # would rather raise an error from here
        # self.authors = None
        raise ValueError('authors passed must be an instance of list')
    else:
      self.authors = None

    Book.__count += 1

  @property
  def price(self): # like a getter function
    return self.__price # return the attribute

  @price.setter
  def price(self, price): # like a setter function
    if price > 0:
      self.__price = price
    else:
      raise ValueError('price passed in must be a non zero positive value')

  @property
  def pages(self):
    return self.__pages

  @pages.setter
  def pages(self, pages):
    if pages > 0:
      self.__pages = pages
    else:
      self.__pages = None

  @staticmethod
  def get_count():
    # non instance function
    return Book.__count

  def get_details(self):
    # instance function
    part1 = 'Title: {0}\nPrice: {1}\nPages: {2}\n'.format(self.title, self.price, self.pages)
    part2 = ''

    if self.authors is not None:
      for author in self.authors:
        part2 += author.get_details() + '\n'
    return part1 + part2

if __name__ == '__main__':

  print(Book.get_count())

  authors = [Author('jane','f',9, Address('US','AZ','some city','23425345')),\
    Author('mehul','m',8)]
  
  b1 = Book('Book 1', 900, 450, authors)
  b1.title = 'Boooook 1' # attribute
  b1.price = -560 # make the attribute as a `property`. price will be a property
  b1.pages = -900
  # b1.pages = 450
  print(b1.get_details())
  # print(b1.pages)


  b2 = Book('Book 2', -450, 1000)
  print(b2.get_details())
  b2.price = 300
  print(b2.get_details())
  print(b2.price)
  b2.price = -560
  print(b2.get_details())
  # print(b2.price)

  print(Book.get_count())















'''class Book:
  def __init__(self, title, price, pages):
    self.title = title
    # private attributes in python
    # they can be accessed only from within the class.
    self.__price = price
    self.__pages = pages

  def get_details(self):
    return 'Title: {0}\nPrice: {1}\nPages: {2}'.format(self.title, self.__price, self.__pages)

  # getter and setters
  def set_price(self, price):
    if price > 0:
      self.__price = price

  def get_price(self):
    return self.__price

if __name__ == '__main__':
  b1 = Book('Book 1', 900, 450)
  # b1.__price = -100 # garbage value. Price should be greater than 0 always
  # b1.pages = -300 # garbage value. Pages should be greater than 0 always
  b1.set_price(-100)

  b1.set_price(1000)
  print(b1.get_details())
  print(b1.get_price())

  # Encapsulation
  # attribute as private
  # getter and setter to access the attribute'''