class Address:
  def __init__(self, country, state, city, postalcode):
    self.country = country
    self.state = state
    self.city = city
    self.postalcode = postalcode

  def get_details(self):
    return 'Country : {0}\nState: {1}\nCity: {2}\nPostal Code : {3}'.format(self.country, self.state\
      ,self.city, self.postalcode)