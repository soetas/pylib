from socket import socket, AF_INET, SOCK_STREAM

class Socket:
  def __init__(self):
    self.st = socket(AF_INET, SOCK_STREAM)

  def bind(self, *, hostname, port):
    self.st.bind((hostname, port))
  
  def listen(self):
    self.st.listen()
  
  def accept(self):
    pass

  def connect(self):
    pass

  def send(self):
    pass

  def close(self):
    pass

  def recv(self):
    pass
