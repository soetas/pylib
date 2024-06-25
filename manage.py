from flask import Flask, request, render_template, redirect, url_for, \
  make_response, json, jsonify, abort
from werkzeug.routing import BaseConverter
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class PathConverter(BaseConverter):
  """custom converter """
  def __init__(self, *args):
    super().__init__(*args)

  def to_python(self, value):
    return value


app = Flask(import_name=__name__)

app.url_map.converters['path'] = PathConverter
app.add_template_filter(lambda value:value.strip('\n\t\r '), 'trim')


@app.route('/')
def index():
  token = request.cookies.get('token')
  return 'hi, flask' if not token == None else redirect(url_for('login'))  


@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
  posts = [
    {},
    {},
    {},
  ]

  if request.method.upper() == 'GET':
    return {
      'code': 200,
      'data': posts,
    }
  else:
    return {}


@app.route('/login', methods=['GET', 'POST'], endpoint='login')
def login():
  method = request.method.upper()

  if method == 'GET':
    return render_template('login.ejs')
  elif method == 'POST':
    username = request.form.get('username')
    passwd = request.form.get('passwd')

    response = make_response(json.dumps({'username':username, 'passwd':passwd}))

    response.mimetype = 'application/json'

    return response


@app.errorhandler(404)
def not_found(err):
  data = {
    'code':404,
    'message':'',
  }

  return render_template('404.ejs', **data)


app.run(host='localhost', port=5713, debug=True)
