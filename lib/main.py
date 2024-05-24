from collections.abc import Iterable, Iterator
from container import Stack, Queue
from net.http import Application, get, post
from builtin import timer
from random import choice
from timeit import repeat
from sys import getsizeof
from gettext import gettext
from functools import reduce


if __name__ == '__main__':
  stack = Stack()
  queue = Queue()

  stack.push(78)
  stack.push(51)
  stack.push(20)

  queue.enqueue(34)
  queue.enqueue(55)
  queue.enqueue(99)

  print(choice(stack), list(reversed(stack)))
  print(99 in stack, bool(queue))

  for item in queue:
    print(item)
  
  print(str(queue))
  print(list(map(lambda x, y:x**y, [78, 12, 10], [1, 2, 3])), (x for x in range(10) if x%2 == 0))

  users = 'jim', 'rose', 'jack'

  print(type(users), stack[:2])
  print(dir(__builtins__))

