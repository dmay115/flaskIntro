# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    """Runs add function on perams a and b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = add(a, b)
    return str(res)

@app.route('/sub')
def sub_route():
    """Runs sub function on perams a and b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = sub(a, b)
    return str(res)

@app.route('/mult')
def mult_route():
    """Runs mult function on perams a and b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = mult(a, b)
    return str(res)

@app.route('/div')
def div_route():
    """Runs div function on perams a and b"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    res = div(a, b)
    return str(res)