from collections import namedtuple, deque
from collections.abc import Iterable, Iterator
from random import choice
from math import hypot, sqrt
from array import array
from timeit import timeit, repeat
from sys import getsizeof
from gettext import gettext

Post = namedtuple('Post', ('id', 'title', 'body'))

class ColorPicker:
  def __init__(self):
    self.colors = [f'rgb({r}, {g}, {b})' for r in range(0, 39) 
                   for g in range(0, 30) 
                   for b in range(0, 30)]
    self.index = 0

  def __getitem__(self, pos):
    return self.colors[pos]

  def __len__(self):
    return len(self.colors)

  def __iter__(self):
    return self

  def __contains__(self, item):
    return item in self.colors

  def __next__(self):
    if self.index < len(self.colors):
      color = self.colors[self.index]
      self.index += 1
      return color
    else:
      self.index = 0
      raise StopIteration


class Number:
  def __init__(self, initial):
    self.value = initial

  def __abs__(self):
    return abs(self.value)

  def __bool__(self):
    return bool(self.value)

  def __add__(self, other):
    return Number(self.value+other.value)

  def __mul__(self, other):
    return Number(self.value*other)

  def __repr__(self):
    return f'Number({self.value})'

def log(message):
  """
  print log message  

  """
  pass


if __name__ == '__main__':
  post = Post(id=0, title='', body='')
  
  colorPicker = ColorPicker()

  print(post[0], post.id)
  print(colorPicker[0], len(colorPicker), choice(colorPicker), 'rgb(0, 0, 0)' in colorPicker)

  for color in colorPicker:
    print(color)
    break

  print(isinstance(colorPicker, Iterable), isinstance(colorPicker, Iterator))
  print(next(colorPicker))

  count = Number(1)

  print(count, count * 5, bool(count), bool(Number(0)), type(b''))

  address = ''

  print(id(address))

  address += 'Malawi'

  print(id(address), ord('A'), chr(126))
  print(list(map(lambda x, y: x**y, [1, 2, 3], [1, 2, 3, 4])))

  # print(repeat('[x for x in range(0, 10) if x%3 == 0]', setup='pass', repeat=3))

  players = 'Elvin Hayes', 'Julius Erving', 'Giannis Antetokounmpo'

  print(type(players))

  users = [
    ('Ora McBride', 'bulwaw@verjosa.sg', [15.4, 96.2, 76.7]),
    ('Chase Franklin', 'sac@rafo.edu', [85.0, 64.1, 88.0]),
    ('Jeffrey Gibbs', 'zo@uloeh.ml', [26.3, 48.9, 43.7])
  ]

  for name, _, scores in sorted(users):
    print(f'{name} => {round(sum(scores)/len(scores), 2)}')
  
  print(Post._fields, post._asdict())
  print(type(slice(0, 10, None)), (9, ))
  
  print(log.__doc__, type(log))

  help(log)
  
