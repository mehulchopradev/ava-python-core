class Book:
  # attribute that is not there with every object
  # should be common to all objects
  __count = 0 # class attribute

  def __init__(self, title, price, pages):
    # instance attributes (object attributes)
    self.title = title
    self.price = price
    self.pages = pages
    Book.__count += 1

  @property
  def price(self): # like a getter function
    return self.__price # return the attribute

  @price.setter
  def price(self, price): # like a setter function
    if price > 0:
      self.__price = price
    else:
      self.__price = None

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
    return 'Title: {0}\nPrice: {1}\nPages: {2}'.format(self.title, self.price, self.pages)

if __name__ == '__main__':

  print(Book.get_count())

  b1 = Book('Book 1', 900, 450)
  b1.title = 'Boooook 1' # attribute
  b1.price = 560 # make the attribute as a `property`. price will be a property
  b1.pages = -900
  # b1.pages = 450
  print(b1.get_details())
  print(b1.pages)


  b2 = Book('Book 2', -450, 1000)
  print(b2.get_details())
  b2.price = 300
  print(b2.get_details())
  print(b2.price)
  b2.price = -560
  print(b2.get_details())
  print(b2.price)

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