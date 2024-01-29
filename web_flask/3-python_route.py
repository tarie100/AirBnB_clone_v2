#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""creating Flask instance"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """defining method"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """defining method"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """defining method"""
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/<text>', strict_slashes=False)
"""defining the route"""
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    """defining method"""
    text = text.replace('_', ' ')
    return 'Python ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """app listening port"""
