from bottle import route, run
from math import *

@route('/hello/<name>')
def index(name):
     return str(eval(name)) # увага! використання eval є небезпечним!

run(host='localhost', port=8080)