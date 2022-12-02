#!/usr/bin/python3
"""Write a script that starts a Flask web application:
    /hbnb: display “HBNB”
    You must use the option strict_slashes=False in your route definition"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """ display Hello HBNB  """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

@app.route("/hbnb", strict_slashes=False)
def Hello_HBNB():
    """ display HBNB  """
    return "“HBNB”"

if __name__ == "__main__":
    app.run(host="0.0.0.0")