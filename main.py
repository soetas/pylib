import fmt
from stdlib import *
from random import seed, randrange, uniform, choices, shuffle

if __name__ == '__main__':
  user = dict(
    account='Theresa Nguyen',
    passwd='123456+',
    token='a57607a2d15d56f59ef3120b8f71b5db'
  )

  print(encrypt(user))
  print(encrypt(user, 'sha1'))
  print(encrypt(user, 'sha256'))

  compress('templates', 'templates')

  url = 'https://fanyi.youdao.com/#/'

  print(Validator.is_email('15530484731@163.com'), Validator.is_url(url))

  fmt.println('hi,python', uniform(60, 100), Random.color())
