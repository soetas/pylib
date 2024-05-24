from collections.abc import Iterable, Iterator
from container import Stack, Queue
from net.http import Application, get, post
from builtin import timer


@get(url='/')
def index():
  return 'hello,world'


@get(url='/api/users')
def user():
  return [
    {},
    {},
    {}
  ]


@post(url='/login')
def login():
  return { 'code': 2000 }


if __name__ == '__main__':
  app = Application()

  app.listen(port=5713, hostname='localhost')
