import json

with open('data/books.json') as fp:
  objs = json.load(fp)
  for obj in objs:
    print(obj['id'])
    print(obj['price'])