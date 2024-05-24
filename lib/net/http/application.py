from http.server import HTTPServer

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
  def __init__(self):
    pass

  def listen(_, *, port, hostname):
    print(routes)
    
  def __call__(self):
    pass

  def __str__(self):
    pass

