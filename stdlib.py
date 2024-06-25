import sys
import json
import pickle
import os
import time
import hashlib
import re
from datetime import datetime, time as datetime_time, timedelta, date
from random import randint
from shutil import copyfileobj, copymode, copystat, make_archive
from zipfile import ZipFile
from logging import debug, info, warn, error, critical, basicConfig, DEBUG, INFO, WARN, \
  Logger, Handler, Filter, Formatter

cwd = os.getcwd()

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

def stringify(value):
  if type(value) in (int, str, float, list, tuple, set, dict):
    return json.dumps(value)
  else:
    return pickle.dumps(value)

def encrypt(payload,  algorithm='md5'):
  payload = pickle.dumps(payload)

  if algorithm == 'md5':
    return hashlib.md5(payload).hexdigest()
  elif algorithm == 'sha1':
    return hashlib.sha1(payload).hexdigest()
  elif algorithm == 'sha256':
    return hashlib.sha256(payload).hexdigest()

def copyfile(src, dst):
  copyfileobj(open(src), open(dst, 'w'))

def compress(name, dirname):
  with ZipFile(f'{name}.zip', 'w') as zipfile:
    for name in os.listdir(dirname):
      zipfile.write(os.path.join(dirname, name))

class Validator:
  @staticmethod 
  def is_email(email):
    return re.match('^\w{5,12}@(qq|163).com$', email) is not None
  
  @staticmethod
  def is_url(url):
    return re.match('^https?://[a-z]{3,}\.[a-z]{3,}\.(com|org|cn)/.+$', url) is not None

class Random:
  @staticmethod
  def color():
    red = hex(randint(0, 255))[2:]
    green = hex(randint(0, 255))[2:]
    blue = hex(randint(0, 255))[2:]

    return f'#{red}{green}{blue}'

  @staticmethod 
  def username():
    pass


def settimeout(callback, seconds):
  time.sleep(seconds)
  callback()

class JSON:
  @staticmethod
  def parse(s_or_fp):
    if type(s_or_fp) is str:
      return json.loads(s_or_fp)
    return json.load(s_or_fp)

  @staticmethod
  def stringify(obj, fp=None):
    if fp is None:
      return json.dumps(obj, indent=2, sort_keys=True)
    json.dump(obj, fp)


class Date:
  def __init__(self, *, year, month, day, hour, minute, second):
    self.date = date(year, month, day)
    self.time = datetime_time(hour, minute, second)

  @staticmethod
  def now():
    return time.time()
  
  def __str__(self):
    return f''

  def get_year(self):
    pass

  def get_month(self):
    pass

  def get_day(self):
    pass

  def get_time(self):
    pass

class Logger:
  def __init__(self, *, level='warn', filename=None):
    level_dict = dict(debug=DEBUG, info=INFO, warn=WARN)
    format = '[%(levelname)s] %(asctime)s %(filename)s: %(message)s'

    basicConfig(level=level_dict[level], filename=filename, format=format)

  def debug(self, msg):
    debug(msg)

  def info(self, msg):
    info(msg)

  def warn(self, msg):
    warn(msg)

  def error(self, msg):
    error(msg)

  def critical(self, msg):
    critical(msg)

