from threading import Thread
import time
from shutil import copy

class CopyThread(Thread):

  def __init__(self, source, destination):
    super().__init__()

    self.source = source
    self.destination = destination

  def run(self): # overriden from the super class
    copy(self.source, self.destination)
    time.sleep(10) # emulate that we are copying a large file
    print('Copying done..')