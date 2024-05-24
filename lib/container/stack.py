class StackIterator:
  index = 0

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
  items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()
  
  def __iter__(self):
    return StackIterator(self.items)
