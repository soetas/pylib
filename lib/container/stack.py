class StackIterator:
  def __init__(self):
    self.index = 0

  def __init__(self, items):
    self.items = items

  def __iter__(self):
    return self

  def __next__(self):
    if self.index < len(self.items): 
      item = self.items[self.index]
      self.index += 1
      return item
    else:
      self.index = 0
      raise StopIteration

class Stack:
  def __init__(self):
    self.__items = []

  def push(self, item):
    self.__items.append(item)

  def pop(self):
    return self.__items.pop()
  
  def __iter__(self):
    return StackIterator(self.__items)

  def __len__(self):
    return len(self.__items)
  
  def __getitem__(self, pos):
    return self.__items[pos]
  
  def __setitem__(self, pos, value):
    self.__items[pos] = value

  def __delitem__(self, pos):
    del self.__items[pos]
  
  def __contains__(self, item):
    return item in self.__items

  def __reverse__(self):
    pass
