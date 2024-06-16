#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:integers>')
def count(integers):
    count = ''
    for i in range(integers):
        count += f'{i}\n'
    return count
# count is an empty string. The empty string has "integer + line break" appended to it for each i in the range of the integers. Then that long string with its line breaks is returned.

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return f'{num1 + num2}'
    elif operation == "-":
        return f'{num1 - num2}'
    elif operation == "*":
        return f'{num1 * num2}'
    elif operation == "div":
        return f'{num1 / num2}'
    elif operation == "%":
        return f'{num1 % num2}'