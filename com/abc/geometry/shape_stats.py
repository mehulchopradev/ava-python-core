import shape
class ShapeStatistics:

  @staticmethod
  def calc_stats(shapeobj):
    if isinstance(shapeobj, shape.Shape):
      print('Area is {0}'.format(shapeobj.area()))
      print('Perimeter is {0}'.format(shapeobj.perimeter()))
    else:
      print('Please pass in something that is Shape')