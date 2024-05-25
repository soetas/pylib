from collections.abc import Iterable, Iterator
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


if __name__ == '__main__':
  stack = Stack()
  app = Application(baseURL='')

  print(stack.__module__, stack.__class__)
  print(stack.__dict__)
  print(Stack.__dict__)

  print(app.info)
 