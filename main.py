from time import time, localtime, strftime, strptime, mktime
from stdlib import settimeout, JSON, Date, Logger

log = Logger(level='warn', filename='system.log')

if __name__ == '__main__':
  birth = strptime('1997-02-22', '%Y-%m-%d')

  print('{}/{:02d}/{}'.format(birth[0], birth[1], birth[2]))
  print(strftime('%H时%M分%S秒', birth), mktime(birth))

  # settimeout(lambda: print('hi,python'), 3)

  todo = dict(
    uid=1,
    id=1,
    title='vue compiler',
    completed=False,
    progress=88.9,
    creator=None
  )

  print(JSON.stringify(todo))

  with open('users.json') as f:
    print(JSON.parse(f)[0]['email'])

  today = Date(year=1997, month=2, day=22, hour=0, minute=0, second=0)

  print(Date.now(), today)

  log.debug('debug')
  log.info('info')
  log.warn('warn')
  log.error('error')
  log.critical('critical')

  # print('\033[1;32;40m' + 'Hello, World!' + '\033[0m')
