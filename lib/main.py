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

class computed:
  def __init__(self, *, type):
    self.type = type

  def __get__(self, instance, owner):
    return self
  
  def __set__(self, instance, value):
    pass

  def __delete__(self, instance):
    pass

class Component:
  display_name = computed(type=str)

  def __getattr__(self, name):
    pass

  def __getattribute__(self, name):
    return super().__getattribute__(name)


if __name__ == '__main__':
  button = Component()

  button.display_name = 'el_button'

  print(type(button.display_name))

