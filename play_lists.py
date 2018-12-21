nos = [5, 6, 3, 4, 2, 2, 1, 10, 6, 7]

# having a new list
# get a new list from nos list containing only the even elements
# filter

# traditionally
even_nos = []
for n in nos:
  if not n % 2:
    even_nos.append(n)
print(even_nos)

# pythonic way
# for comprehensions
even_nos = [n for n in nos if not n % 2]
print(even_nos)

odds_3 = [n for n in nos if n % 2 and n > 3]
print(odds_3)

# having a new list
# get a new list from nos list containing the squares of all the elements
# mapping

# traditionally
squares = []
for n in nos:
  squares.append(n ** 2)

print(squares)

# pythonic way
# for comprehensions
squares = [n ** 2 for n in nos]
print(squares)



