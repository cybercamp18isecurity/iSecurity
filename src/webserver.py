import flask
import os
myPath = os.path.dirname(os.path.abspath(__file__))

from flask import jsonify

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def menu():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
