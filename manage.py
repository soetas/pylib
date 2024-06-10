from flask import Flask, request

app = Flask(import_name=__name__)

@app.route('/')
def index():
  return 'hi, flask!'

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
  if request.method.upper() == 'GET':
    return [
      {},
      {},
      {}
    ]
  else:
    return {}
  

app.run(host='localhost', port=5713, debug=True)
