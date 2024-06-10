import json
import math
from vendor.bottle import route, run, get, post, request, static_file, error, \
  abort, redirect, response, Response, template
from pathlib import Path
from urllib.parse import quote, unquote

mime = {
  'html':'text/html',
  'css':'text/css',
  'js': 'application/javascript',
  'jpg':'image/jpeg',
}

cookie_secret = 'bf5ded17-92f6-5ef6-b8d6-9433c225d116'

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __abs__(self):
    return abs(math.hypot(self.x, self.y))


@route('/', method='GET')
def index():
  response.set_cookie('token', '84c7985a-dd4e-52c4-bba9-c4d5fb3b9278', secret=cookie_secret)

  data = {
    'greet':'hey',
    'framework':'<em>bottle</em>',
    'vector':Vector(3, 4)
  }

  return template('{{ greet }}, {{ !framework }} {{ abs(vector) }}', **data)


@get()
@route('/api/')
def api():
  token = request.get_cookie('token', secret=cookie_secret)
  response.add_header('Content-Type', 'application/json; charset=utf-8')

  return json.dumps({
    'apis':['posts', 'users', 'todos'],
    'token': token,
  })


@route('/api/posts/<id:int>', method=['GET', 'POST'])
def posts(id=0):
  posts = [
    {},
    {},
    {},
    {},
    {}
  ]

  response.add_header('Content-Type', 'application/json')

  if request.method.upper() == 'GET':
     return json.dumps(posts)
  else:
    return {}

@route('/api/users', method=['GET', 'POST'])
def users():
  users = [
    {},
    {},
    {}
  ]

  if request.method.upper() == 'GET':
    skip = int(request.query['skip'])
    limit = int(request.query['limit'])

    return {
      'skip': skip,
      'limit': limit,
    }
  else:
    username = request.forms['username']
    email = request.forms['email']
    return {'username':username, 'email':email}


@route('/public/<path:path>')
def static(path:str):
  *sub_paths, filename = path.split('/')
  _, ext = filename.split('.')
  
  download = ext in ['jpg', 'png', 'gif']

  if not Path.joinpath(Path.cwd(), f'public/{path}').exists():
    abort(404, '')

  return static_file(filename=filename, root=f'public/{"/".join(sub_paths)}', mimetype=mime[ext], 
                     download=download)

@route('/profile')
@get()
@post()
def profile():
  if request.method.upper() == 'GET':
    return '''
    <form action="/profile" method="post" enctype="multipart/form-data">
      <p>
        <input type="file" name="avatar" >
      </p>
      <button type="submit">submit</button>
    </form>
    '''
  else:
    avatar = request.files['avatar']
    _, ext = avatar.raw_filename.split('.')

    try:
      avatar.save(f'upload/{avatar.name}.{ext}')
    except Exception as ex:
      return {'status':'fail'}
    else:
      return {'status':'success'}

@error(404)
def not_found(err):
  return '404'


if __name__ == '__main__':
  run(server='tornado', host='localhost', port=5713, debug=True, reloader=True)

