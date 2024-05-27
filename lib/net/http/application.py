from http.server import HTTPServer
from typing import Any

routes = {
  "get":[],
  "post":[],

}

def get(*, url):
  def inner(handler):
    response = handler()
    routes['get'].append((url, response))
  return inner


def post(*, url):
  def inner(handler):
    response = handler()
    routes['post'].append((url, response))
  return inner  


class readonly:
  def __init__(self):
    self.value = None

  def __get__(self, instance, owner):
    pass

  def __set__(self, instance, value):
    pass

  def __delete__(self, instance):
    pass

class validate:
  def __init__(self, *, type, max, min, max_length, min_length):
    self.type = type
    self.value = None

  def __get__(self, instance, owner):
    pass

  def __set__(self, instance, value):
    if isinstance(value, self.type):
      pass
    else:
      raise TypeError()

  def __delete__(self, instance):
    pass


class Application:
  """
  
  """
  # 自省机制
  __slots__ = ('baseURL')

  def __init__(self, *, baseURL):
    super().__init__()
    self.baseURL = baseURL

  def listen(_, *, port, hostname):
    print(routes)
    
  def __call__(self):
    pass

  def __str__(self):
    pass

  def __del__(self):
    pass

  def __getattribute__(self, name):
    return object.__getattribute__(self, name)

  def __getattr__(self, name):
    pass

  @property
  def info(self):
    return { 'version':'0.0.1', 'status':'run' }
  
  @info.setter
  def info(self, value):
    pass

  @info.deleter
  def info(self):
    pass

  @staticmethod
  def getInstance():
    return Application()
  