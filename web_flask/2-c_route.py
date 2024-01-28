#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)
"""create Flask instance"""

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """define method"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """deine method"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def show_text(text):
    """define method"""
    text = text.replace('_', ' ')
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    """app listening port"""
