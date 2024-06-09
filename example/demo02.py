import sys
from abc import abstractmethod, ABCMeta
from collections.abc import Sized
from threading import Thread

class Array(Sized):
  __maxsize = sys.maxsize 
  __slots__ = ('items', 'pos', )

  def __init__(self, items):
    self.items = list(items)
    self.pos = 0

  def __len__(self):
    return len(self.items)
  
  def __getitem__(self, pos):
    return self.items[pos]

  def __iter__(self):
    return self

  def __next__(self):
    if self.pos < len(self.items):
      item = self.items[self.pos]
      self.pos += 1
      return item
    else:
      self.pos = 0
      raise StopIteration

  def __repr__(self):
    return f'Array{{{", ".join(str(item) for item in self.items)}}}'

  def __add__(self, other):
    return Array(self.items + list(other))

class Node:
  pass

class Document(Node):
  pass

class Element(Node, metaclass=ABCMeta):
  @abstractmethod
  def render(self):
    raise NotImplementedError

class HTMLDocument(Document):
  pass

class HTMLElement(Element):
  pass

class HTMLInputElement(HTMLElement):
  pass

class HTMLParagraphElement(HTMLElement):
  pass

class HTMLAnchorElement(HTMLElement):
  def __init__(self, href, target):
    self.href = href
    self.target = target

  def __str__(self):
    return f'<a href="{self.href}" target="{self.target}"></a>'

  def render(self):
    pass

class DocumentFragment(HTMLDocument, HTMLElement):
  pass

class HTTPClient:
  def __init__(self):
    self.base_url = ''
    self.timeout = 50

  @classmethod
  def create(cls, *, base_url, timeout):
    instance = cls()
    instance.base_url = base_url
    instance.timeout = timeout
    return instance

  def get(self):
    pass

  def post(self):
    pass

  @staticmethod
  def request(*, url, method, headers):
    pass  


if __name__ == '__main__':
  arr = Array(range(1, 10, 2))

  for x in arr:
    print(x, end=' ')

  print('\n', len(arr), sep='')
  print(arr[:2], arr, arr + (12, 67, 29), type({}))

  link = HTMLAnchorElement('', '_self')

  link.render()

  print(link, hasattr(link, 'render'))
  print(HTMLAnchorElement.__bases__, HTMLAnchorElement.__mro__)
  print(isinstance(link, HTMLElement), type(link) is HTMLElement)
  print(Array._Array__maxsize)
  print(DocumentFragment.mro())

  client = HTTPClient.create(base_url='', timeout=1000)

  print(client.request is HTTPClient.request)
  print(client.__dict__)



  