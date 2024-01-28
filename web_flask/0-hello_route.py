#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
"""creat Flask instance"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """define method"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
    """app listening port"""
