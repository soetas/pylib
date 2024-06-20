import sys
import net

config = {}

def printf(format: str, *args: tuple) -> None:
  pass


def init(*, host: str='127.0.0.1', port: int) -> None:
  global config
  config = dict(host=host, port=port)


def rand_color() -> str:
  return f'#193411'

class ChatRot:
  platform = 'win'

  def __init__(self, nickname):
    super().__init__()
    self.nickname = nickname

  def __str__(self):
    return super().__str__()

  def __copy__(self):
    pass

  def __class__(self):
    pass

  @classmethod
  def new(cls):
    return cls('')

  
if __name__ == '__main__':
  server = net.Socket()

  

