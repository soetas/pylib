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


class Application:
  """
  
  """
  __slots__ = ('baseURL')
  version = '0.0.1'

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

  @property
  def info(self):
    return { 'version':'0.0.1', 'status':'run' }
  
  @info.setter
  def info(self, value):
    pass

  @info.deleter
  def info(self):
    pass
