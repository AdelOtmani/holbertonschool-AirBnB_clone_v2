#!/usr/bin/python3
"""Write a script that starts a Flask web application:
/python/<text>: display “Python ”, followed by the value of the text variable
(replace underscore _ symbols with a space )
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """ display Hello HBNB  """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ display HBNB  """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ display C + text and replace "_" by " " """
    text = text.replace("_", " ")
    return "C {}".format(text)
    

@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ display Python + text and replace "_" by " " """
    text = text.replace("_", " ")
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
