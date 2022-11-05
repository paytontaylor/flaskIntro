# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operation = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<func>/<int:a>/<int:b>')
def do_math(func,a,b):
    function = operation[func]
    result = function(a,b)
    return str(result)

# @app.route('/add')
# def add_nums():
#     """ Adds a and b params """
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     res = add(a,b)
#     return str(res)


# @app.route('/sub')
# def sub_nums():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     res = sub(a,b)
#     return str(res)


# @app.route('/mult')
# def mult_nums():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     res = mult(a,b)
#     return str(res)

# @app.route('/div')
# def div_nums():
#     a = int(request.args['a'])
#     b = int(request.args['b'])
#     res = div(a,b)
#     return str(res)