from os.path import basename
from shutil import copy

source_file_path = input('enter source : ')
destination_dir = input('enter destination : ')

destination_file_path = destination_dir + '/' + basename(source_file_path)

'''with open(source_file_path, mode='rb') as fs:
  with open(destination_file_path, mode='wb') as fd:
    fd.write(fs.read())'''

copy(source_file_path, destination_file_path)