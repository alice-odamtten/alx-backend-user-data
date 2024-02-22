#!/usr/bin/env python3
'''set up a basic Flask app'''

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    '''defualt page'''
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")