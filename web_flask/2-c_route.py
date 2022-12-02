#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """ display Hello HBNB  """
    return  "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def Hello_HBNB():
    """ display HBNB  """
    return  "“HBNB”"

@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ display C + text and replace "_" by " " """
    text = text.replace("_", " ")
    return  "C"+str(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")