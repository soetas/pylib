import sys
import json
import pickle
import os
import time
from datetime import datetime
from random import randint

cwd = os.getcwd()
today = datetime.now()


class Command:
  def name(self, name):
    pass

  def description(self, desc):
    pass

def env():
  env_info = dict(version=sys.version, maxsize=sys.maxsize, path=sys.path, 
                  platform=sys.platform, copyright=sys.copyright, 
                  default_encoding=sys.getdefaultencoding(), filesystem_encoding=sys.getfilesystemencoding(),
                  recursion_limit=sys.getrecursionlimit())

  return json.dumps(env_info, indent=2)

def quit():
  sys.exit(0)

def is_dir(path):
  if os.path.exists(path) and os.path.isdir(path):
    return True
  return False

def exec(command):
  os.system(command)

def now():
  timestamp = time.time()
  current_time = time.localtime(timestamp)
  
  year = current_time.tm_year
  month = current_time.tm_mon
  day = current_time.tm_mday

  return f'{year}-{month:02}-{day} {time.strftime("%H:%M:%S", current_time)}'

def rand_color():
  red = hex(randint(0, 255))[2:]
  green = hex(randint(0, 255))[2:]
  blue = hex(randint(0, 255))[2:]

  return f'#{red}{green}{blue}'

def stringify(value):
  if type(value) in (int, str, float, list, tuple, set, dict):
    return json.dumps(value)
  else:
    return pickle.dumps(value)
