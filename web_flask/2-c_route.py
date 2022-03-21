#!/usr/bin/python3
"""script that starts a Flask web application
web app must be listening on 0.0.0.0:5000
/: will display "Hello HBNB!"
/hbnb: will display “HBNB”
must use sctrict_slashes=False in route
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
