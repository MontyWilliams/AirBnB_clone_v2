#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """tears down database
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """returns HTML page
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
