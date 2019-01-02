from shutil import copy
from os.path import basename
from series import fibo_series
# from threading import Thread
from copy_thread import CopyThread
import time

'''def copy_files(source, destination):
  # IO
  copy(source, destination)
  time.sleep(10) # emulate that we are copying a large file
  print('Copying done..')'''

source_file_path = input('enter source : ')
destination_dir = input('enter destination : ')
n = int(input('Enter n : '))
destination_file_path = destination_dir + '/' + basename(source_file_path)

ct = CopyThread(source_file_path, destination_file_path)
ct.start()
'''udt = Thread(target=copy_files, args=(source_file_path, destination_file_path))
udt.start()'''

# CPU operation (non IO)
series = fibo_series(n)
print(series)