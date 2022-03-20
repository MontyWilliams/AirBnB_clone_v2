#!/usr/bin/python3
"""script that starts a Flask web application
web app must be listening on 0.0.0.0:5000
/: will display "Hello HBNB!"
must use sctrict_slashes=False in route
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
