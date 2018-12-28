# file_path = 'professor.py' # relative to read_files
file_path = '/Users/mehul.chopra/Documents/personal/training/ava-python/professor.py' # absolute path

fd = open(file_path)

# printing line by line frm the file
# the for loop on a file is file pointer sensitive
for line in fd: # fd can be considered to be having a sequence of lines
  print(line)

print('After the loop')
for line in fd: # will print nothing as because of the above loop, the internal fp has reached EOF
  print(line)

fd.seek(0) # moves the internal fp to the start of the file

print('After resetting')
for line in fd:
  print(line)
# the internal fp now again has come to the EOF

fd.seek(0)

lines = fd.readlines()
for line in lines:
  print(line, end='')

# internal fp has come to the EOF
fd.seek(0)
print()

line = fd.readline() # reading a single line
print(line)

fd.seek(0)

print('Entire file is read in a str object {0}'.format(fd.read()))

fd.close()

file_path = 'play.py'
with open(file_path) as fd:
  print(fd.read())

# after coming out of the above `with` block, the reference to the file will be closed automatically