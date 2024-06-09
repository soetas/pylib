import json
from vendor.bottle import route, run, get, post, request

@route('/', method='GET')
def index():
  return 'hi, bottle'


@get()
@route('/api/')
def api():
  return json.dumps(['posts', 'users', 'todos'])


@route('/api/posts', method=['GET', 'POST'])
def posts():
  if request.method.upper() == 'GET':
     return json.dumps([
      {},
      {},
      {}
    ])
  else:
    return json.dumps({})
 

if __name__ == '__main__':
  run(host='localhost', port=5713, debug=True, reloader=True)

