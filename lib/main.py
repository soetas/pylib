import threading
from collections.abc import Iterable, Iterator, Sized, Sequence, MutableSequence
from abc import ABC, abstractmethod
from random import choice
from timeit import repeat
from sys import getsizeof
from gettext import gettext
from functools import reduce
from container import Stack, Queue
from net.http import Application, get, post, HTTPClient
from builtin import timer

# dynamically bind custom object methods
from types import MethodType 
from contextlib import contextmanager

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
def parse():
  pass



if __name__ == '__main__':
  mul = lambda x,y: x*y

  print(id(mul), type(mul), type(type(mul)))
  print(type(Application), typeof(0))  

  count = num(-0.8)

  print(type(count), count, abs(count))
  print(num.__bases__)
  print(type(num), type(type), type(None), None == None)
  print(repr(count), bool(num(0)))

  mongodb = Mongodb()

  print(isinstance(mongodb, Database), type(mongodb) is Database)
  print(issubclass(Mongodb, Database))

  print(Application.__mro__)

  HTTPClient.request()

  with Cheerio('') as cheerio:
    print(cheerio)


