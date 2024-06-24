import time
import pytz
import json
from os import getenv, environ, pathsep, linesep, stat
from os.path import abspath, isabs, getatime, getsize
from collections import namedtuple
from datetime import timedelta
from random import sample
from string import digits, ascii_lowercase
from stdlib import *


User = namedtuple('User', ('name', 'email', 'birth'))

if __name__ == '__main__':
  print(cwd, is_dir('..'))
  print(abspath(__file__), getenv('GOPROXY'))

  exec('ls .')

  print(now())

  user = User(name='', email='', birth=time.strptime('1997/02/22', '%Y/%m/%d'))

  print(user.birth)
  print(today)
  print([timezone for timezone in pytz.all_timezones if timezone.startswith('Asia')])
  
  print(rand_color())

  char_list = list(ascii_lowercase)+list(digits)

  print(''.join(sample(char_list, 4)))

  post = dict(
    uid=0, 
    id=0, 
    author=None,
    title='learn vue', 
    body='vue is front-end progressive framework', 
    tags=['vue', 'frontend', 'framework']
  )

  print(pickle.dumps(post))
  print(json.dumps(post).encode('utf8'))

  with open('posts.json', 'w+') as f:
    json.dump(post, f, indent=2)

  # with open('users.txt') as f:
  #   pickle.dump(user, f)

  print(environ.get('GOPATH'), pathsep, stringify(linesep))
  print(stat('README.md').st_size, isabs('.'))
  print(time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(getatime('note.md'))))
  print(getsize('README.md'))
  
  exec('cat LICENSE')
  exec('ipconfig')


  