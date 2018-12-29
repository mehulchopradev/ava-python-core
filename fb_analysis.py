from csv import reader, DictReader

username_in_dict = {}

'''with open('data/fb_logs.csv') as fp:
  fbreader = reader(fp)
  seenfirstline = False
  for row in fbreader:
    if not seenfirstline:
      seenfirstline = True
    else:
      username, action = row[0], row[-1]
      if action == 'in':
        if username in username_in_dict:
          username_in_dict[username] = username_in_dict[username] + 1
        else:
          username_in_dict[username] = 1

print(username_in_dict)'''

'''with open('data/fb_logs.csv') as fp:
  dr = DictReader(fp)
  for row in dr:
    username, action = row['username'], row['action']
    if action == 'in':
      if username in username_in_dict:
        username_in_dict[username] = username_in_dict[username] + 1
      else:
        username_in_dict[username] = 1

print(username_in_dict)'''

username_actions_dict = {}
with open('data/fb_logs.csv') as fp:
  dr = DictReader(fp)
  for row in dr:
    username, action = row['username'], row['action']
    if (username, action) in username_actions_dict:
      username_actions_dict[(username, action)] += 1
    else:
      username_actions_dict[(username, action)] = 1

print(username_actions_dict)

