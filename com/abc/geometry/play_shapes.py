import rectangle
import shape_stats
import square

r = rectangle.Rectangle(5, 3)

shape_stats.ShapeStatistics.calc_stats(r)

s = square.Square(5)
shape_stats.ShapeStatistics.calc_stats(s)