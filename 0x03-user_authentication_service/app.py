#!/usr/bin/env python3
'''set up a basic Flask app'''
from auth import Auth
from flask import Flask, jsonify, request, make_response, abort
app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def hello():
    '''defualt page'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    '''the end-point to register a user'''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    '''login route'''
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    '''the logout route'''
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
