class Queue:
  def __init__(self, items=[]):
    self.index = 0
    self.items = items

  def enqueue(self, item):
    self.items.append(item)
  
  def dequeue(self):
    return self.items.pop(0)    

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

  def __bool__(self):
    return bool(len(self.items))
   
  def __len__(self):
    return len(self.items)
   
  def __str__(self):
    return f"Queue { { ', '.join([str(item) for item in self.items]) } }"

