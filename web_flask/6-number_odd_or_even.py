#!/usr/bin/python3
"""Write a script that starts a Flask web application:
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
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
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ display C + text and replace "_" by " " """
    text = text.replace("_", " ")
    return "C"+str(text)

@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ display Python + text and replace "_" by " " """
    text = text.replace("_", " ")
    return "Python"+str(text)

@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """ display n """
    return "{} is a number".format(n)

@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """ display n """
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    """ display n """
    return render_template("6-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")