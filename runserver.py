from flask import Flask
from os import environ

app = Flask(__name__)

app.secret_key = '*gnj8'

@app.route('/hello')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    HOST = environ.get('IP')
    PORT = int(environ.get('PORT'))
    app.run(HOST, PORT, debug=True)