from contextlib import contextmanager
from collections import deque, UserDict, defaultdict, Iterable, Iterator
from array import array
from collections.abc import Sequence, MutableSequence, Mapping, MutableMapping, MutableSet, Set
from numbers import Integral
from copy import deepcopy

__all__ = ()

class Storage:
  def __enter__(self):
    return self

  def __exit__(self, *args):
    pass
  
  def set(self, key, value):
    pass

  def get(self, key):
    pass

  def remove(self, key):
    pass


@contextmanager
def fetch(url: str, method: str):
  """

  Parameters:

  Returns:

  """
  yield {}

class Stack:
  def __init__(self, iter=None):
    self.items = list(iter)
    self.pos = 0

  def __getitem__(self, pos):
    if isinstance(pos, slice):
      return Stack(self.items[pos])
    else:
      return self.items[pos]

  def __reversed__(self):
    pass
  
  def __len__(self):
    pass

  def __iter__(self):
    return self

  def __next__(self):
    try:
      item = self.items[self.pos]
      self.pos += 1
    except IndexError:
      self.pos = 0
      raise StopIteration
    return item

  def __contains__(self, item):
    pass

  def __eq__(self, other):
    pass

  def __del__(self):
    pass


class Readonly:
  def __init__(self, initial):
    self.__value = initial

  def __get__(self, instance, owner):
    return self.__value
  
  def __set__(self, instance, value):
    raise 'field is readonly'

  def __delete__(self, instance):
    pass


class HTTPSimpleServer:
  version = Readonly('0.0.1')

  def __new__(cls, *args, **kwargs):
    return super().__new__(cls)

  def __init__(self, *, hostname, port):
    self.hostname = hostname
    self.port = port
  
  @property 
  def address(self):
    return f'{self.hostname}:{self.port}'
  
  @address.setter
  def address(self, value):
    self.hostname, self.port = value.split(':')

  def __getattr__(self, name):
    raise KeyError(f'\"{name}\" is not exist')
  
  def __getattribute__(self, name):
    return super().__getattribute__(name)


Employee = type('Employee', (object, ), {
  'first_name': 'Derrick',
  'last_name':'Sanchez',
  '__str__': lambda self: f'{self.first_name} {self.last_name}',

})

Programmer = type('Programmer', (Employee, ), {})


if __name__ == '__main__':
  with Storage() as storage:
    print(storage)

  with fetch('') as result:
    print(result)

  arr = array('f', [78, 67, 99, 60, 93])

  arr.append(89)

  print(arr, type(x for x in range(10)))
  
  users = [
    {'account':'Estella Boyd', 'email':'vovo@minduma.lv', 'points':72},
    {'account':'Brent Taylor', 'email':'bes@cazabibod.com', 'points':75},
    {'account':'Sara Brady', 'email':'poco@atoada.ci', 'points':96},
    {'account':'Dustin Walters', 'email':'wovdikmo@utebas.zw', 'points':38},
    {'account':'Claudia Fleming', 'email':'ozisoj@kadevca.mx', 'points':42},
  ]

  print([{k:v for k, v in user.items() if k != 'points'} 
         for user in users if user['points'] >= 60])
  
  player = {
    'name':'Tom Quinn',
    'rate': 9.4,
    'address':{
      'country':'Zimbabwe'
    }
  }
  
  other_player = deepcopy(player)
  # other_player = player.copy()

  other_player['address']['country'] = 'U.S. Outlying Islands'

  print(player)

  emails = set(('le@ohabeb.ss', 'wukvihi@lijrab.ba', 'reozcaj@mejdamvi.sm', 'wukvihi@lijrab.ba', ))
  emails.add('nogi@iw.ag')

  print(emails, [1, ] == [1, ])
  print(Stack.__init__.__defaults__)

  server = HTTPSimpleServer(hostname='0.0.0.0', port=5713)

  server.address = '127.0.0.1:8080'

  print(server.address, getattr(server, 'version'))
  
  employee = Employee()

  print(employee, Programmer.mro())

  stack = Stack([67, 19, 45, 10, 99])

  for item in stack:
    print(item)

  print(next(stack))

  fetch()