from pathlib import Path

class HTTPServer:
  def __init__(self):
    super().__init__()
    self.port = 5713

  @property
  def port(self):
    return self.__port

  @port.setter
  def port(self, value):
    if not 1024 <= value <= 49151:
      raise ValueError('')
    self.__port = value  
  
  def __str__(self):
    return f'<{__name__}.{type(self).__name__} object at {hex(id(self))}>'

class Widget:
  def __init__(self, display):
    self.display = display

class Button(Widget):
  def __init__(self, type, disabled):
    super().__init__('inline-block')
    self.type = type
    self.disabled = disabled
    
class Reader:
  def read(self, prompt, type):
    return type(input(prompt))

class Writer:
  def write(self, content, end='\n'):
    print(content, end=end)

class Terminal(Reader, Writer):
  def __init__(self):
    super().__init__()

class File:
  def __init__(self):
    self.base = Path.cwd()

  def read(self, path):
    path = Path.joinpath(self.base, path)

    if not (path.is_file() and path.exists()):
      raise FileExistsError()

    with open(path, 'rt') as stream:
      return ''.join(stream.readlines())


if __name__ == '__main__':
  users = [
    {'account':'Sadie Mullins', 'email':'podeba@cimjugcoz.bs', 'gpa':17},
    {'account':'Theresa Burton', 'email':'cebluhe@bes.ec', 'gpa':28},
    {'account':'Dale Weber', 'email':'dapiara@sod.gw', 'gpa':55}
  ]

  users.sort(key=lambda item:len(item['account']))

  print(users)

  server = HTTPServer()

  print(server, server.port, server.__dict__)
  print(Button('submit', False).__dict__)

  terminal = Terminal()

  print(terminal)

  score = terminal.read('enter your score: ', float)

  terminal.write(f'score: {score}')

  fs = File()

  print(fs.read('README.md'))

