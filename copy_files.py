# program runs in a process
# In the process, the program runs in a single thread (LWP)

from os.path import basename
from shutil import copy
from series import fibo_series

source_file_path = input('enter source : ')
destination_dir = input('enter destination : ')
n = int(input('Enter n : '))

destination_file_path = destination_dir + '/' + basename(source_file_path)

'''with open(source_file_path, mode='rb') as fs:
  with open(destination_file_path, mode='wb') as fd:
    fd.write(fs.read())'''

# IO operation (no CPU involvement)
# can take time when copying large files
copy(source_file_path, destination_file_path)


# CPU operation (non IO)
series = fibo_series(n)

print(series)