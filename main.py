class App:
  def __init__(self, name, mark):
    self.__name = name
    self.mark = mark

  @property
  def mark(self):
    return self.__mark

  @mark.setter
  def mark(self, value):
    if not 0 <= value <= 5:
      raise ValueError('')
    
    self.__mark = value

  def __del__(self):
    pass

  def __str__(self):
    return f'App{{name:{self.__name}, mark:{self.__mark}}}'

  def __repr__(self):
    return f'<{__name__}.{type(self).__name__} object at 0x00000{hex(id(self))[2:].upper()}>'

  def install(self):
    pass

  def upgrade(self):
    pass

  def uninstall(self):
    del self

class Software:
  def run(self):
    pass

class SocialApp(App, Software):
  def __init__(self, name, mark, version):
    super().__init__(name, mark)
    self.version = version

  def __str__(self):
    desc = super().__str__()
    return f'{desc[:len(desc)-1]}, version:{self.version}}}'


if __name__ == '__main__':
  account = 'Lou Hopkins' or input('account: ')
  email = 'dungok@az.hm' or input('email: ')

  post = dict(uid=0, id=0, title='', body='')

  print(f'<{account}, {email}>', post)

  app = SocialApp('wechat', 4.1, '1.16.2')

  print(app, SocialApp.mro())
  print(isinstance(app, App))


  
