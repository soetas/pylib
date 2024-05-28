"""
@author soetas
@file main.py
@since 2024/05/28 9:10
"""
import threading
import copy
from collections.abc import Iterable, Iterator, Sized, Sequence, MutableSequence, \
  Mapping, MutableMapping
from abc import ABC, abstractmethod
from random import choice
from timeit import repeat
from sys import getsizeof
from gettext import gettext
from functools import reduce
from container import Stack, Queue, array
from net.http import Application, get, post, HTTPClient
from builtin import timer

# dynamically bind custom object methods
from types import MethodType 
from contextlib import contextmanager
from bisect import bisect, insort
from collections import UserDict

def typeof(value):
  return type(value).__name__


@get(url='/')
def index():
  pass

def __init__(self, initial):
  self.value = initial

def __str__(self):
  return f'{self.value}'

def __repr__(self):
  return '{!r}'.format(self.value)

def __abs__(self):
  return abs(self.value)

def __bool__(self):
  return bool(self.value)

def __iadd__(self):
  pass


num = type('num', (object, ), {
  '__init__': __init__,
  '__str__':__str__,
  '__repr__':__repr__,
  '__abs__':__abs__,
  '__bool__':__bool__,
  '__iadd__':__iadd__,

})

symbol = type('symbol', (), {})

class Database(ABC):
  @abstractmethod
  def query(self, sql):
    pass

class Mysql(Database):
  def query(self, sql):
    pass

class Sqlite(Database):
  def query(self, sql):
    pass

class Mongodb(Database):
  def query(self, sql):
    super().query(sql)

class Cheerio:
  def __init__(self, startURL):
    self.startURL = startURL

  def __enter__(self):
    return self

  def __exit__(self, *args):
    pass

@contextmanager
def read_file():
  print('enter ~~~')
  yield 0
  print('exit ~~~')

class Map(UserDict):
  pass


def fibonacci(n):
  pass


if __name__ == '__main__':
  print(list(range(0, 10, 2))[::-1])
  print(array('d', [81, 67, 10, 55, 28]))

  square = lambda x: x**2

  print([square(x) for x in range(1, 10) if x%2 == 0])
  print(next(filter(lambda x: x>0, (-5, 7, -1, 9))))
  print(dir(dict))
  help(dict.fromkeys)

  user = {
    'account':'Jeanette Bishop',
    'passwd':'2d1c2641-4ebe-53da-be10-53527bb3b434',
    'email':'bo@ridha.ch'
  }

  for key, value in user.items():
    print(f'{key} => {value}')

  print(set('hello,world'))
  print(dir(set))

  print(isinstance((x for x in range(10)), Iterator))

  users = [
    {'name':'Tom Smith', 'email':'foemlu@jut.ec', 'points':7},
    {'name':'Elmer Banks', 'email':'vuewe@ig.ph', 'points':18},
    {'name':'Bernard West', 'email':'kivudut@vejse.il', 'points':4},
    {'name':'Bettie Nash', 'email':'hi@gih.ht', 'points':21},
    {'name':'Katharine Gilbert', 'email':'tool@genuza.li', 'points':10},
  ]

  vip_users = (user for user in users if user['points'] >= 10)

  print(vip_users, type(vip_users))
  
  for user in vip_users:
    print(user)

  try:
    print(next(vip_users))
  except StopIteration as e:
    print(e)
  else:
    pass
  finally:
    pass

  with read_file() as obj:
    pass
