#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""creating Flask instance"""


@app.route('/', strict_slashes=False)
"""defining route"""
def hello_hbnb():
    """defining method"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    text = text.replace('_', ' ')
    return 'Python ' + text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """app listening port"""
