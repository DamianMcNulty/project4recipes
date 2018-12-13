from os import environ
from flask import Flask

app = Flask(__name__)

app.secret_key = environ.get('SECRET_KEY')

@app.route('/hello')
def hello():
    return "Hello, World!"

if environ.get('DEVELOPMENT'):
    development = True
else:
    development = False

if __name__ == '__main__':
    HOST = environ.get('IP')
    if development:
        PORT = int(environ.get('C9_PORT'))
    else:
        PORT = int(environ.get('PORT'))
    app.run(HOST, PORT, debug=development)