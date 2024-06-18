import sys
from typing import List
from logging import warning, exception, basicConfig, INFO, getLogger

basicConfig(level=INFO)

log = getLogger()

class HTTPClient:
  __instance = None
  __version = '1.1'

  def get():
    pass
  
  def post():
    pass

  @staticmethod
  def request():
    pass

  @classmethod
  def create(cls, *, baseURL, timeout):
    if cls.__instance == None:
      cls.__instance = cls()
    return cls.__instance

class Math:
  Pi = 3.1415926

  @staticmethod
  def pow(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
      raise TypeError
    return x ** y

class GarbageCollector:
  __instance = None

  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self, status, *, version):
    self.status = status
    self.version = version

class Rune:
  @staticmethod
  def __normalize(value):
    if isinstance(value, Rune):
      return value.code
    elif isinstance(value, str):
      return ord(value)
    elif isinstance(value, int):
      return value
    else:
      raise TypeError('')

  def __init__(self, value):
    self.code = value if isinstance(value, int) else ord(value)

  def __add__(self, other):
    return Rune(self.code + other)

  def __sub__(self, other):
    return Rune(self.code - other)

  def __cmp__(self, other):
    if self.code > other.code:
      return 1
    elif self.code < other.code:
      return -1
    else:
      return 0

  def __lt__(self, other):
    return self.code < other.code

  def __str__(self):
    return f'Rune({chr(self.code)})'

  def __repr__(self):
    return f'{chr(self.code)}'

class OverflowError(Exception):
  def __init__(self):
    super().__init__()
  
  def __str__(self):
    return f'overflow'
  

if __name__ == '__main__':
  try:
    raise OverflowError()
  except OverflowError as ex:
    print(ex)

  try:
    with open('request.http', 'r+') as f:
      print(f.readlines())
  except (FileNotFoundError, Exception):
    pass

  print(FileNotFoundError.mro())

