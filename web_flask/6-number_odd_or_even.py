#!/usr/bin/python3
"""script that starts a Flask web application
web app must be listening on 0.0.0.0:5000
/:  display's "Hello HBNB!"
/hbnb:  display's “HBNB”
must use sctrict_slashes=False in route
/c:  display's “C ” followed by the value text variable
/python:  display's " Python " followed by text variable --
     has default value of "is cool"
"""

from flask import Flask, render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonischeatmode(text="is cool"):
    """display “Python ” followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def printints(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberTemplate(n):
    """ display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddOrEven(n):
    """ display a HTML page only if n is an integer"""
    if n % 2 == 0:
        o = "even"
    else:
        o = "odd"
    return render_template('6-number_odd_or_even.html', n=n, o=o)




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
