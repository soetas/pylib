from time import time

def timer(label):
  startTime = time()
  def end(format):
    nonlocal label
    endTime = time()
    print(f'{ label }: { endTime-startTime }s')

  return end
