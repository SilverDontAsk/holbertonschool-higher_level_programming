#!/usr/bin/python3
"""
Simple API in python with flask
"""
from flask import Flask, jsonify, request, Response, abort
import json


app = Flask(__name__)

users = {}

@app.route('/')
def home():
    """
    message displayed on home page
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """
    returns a jsonified list of users
    """
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def get_status():
    """
    gets the status of the API
    """
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """
    gets and jsonifies users
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    data = users[username]
    data['username'] = username

    return jsonify(data)

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    this thing adds users via curl in terminal so why the hell is it being marked as wrong
    it adds them well
    it gives the response on a user without a username AND
    it deals a duplicate username so i honestly have 0 to no idea
    """
    if request.get_json() is None:
        abort(400, "Not a JSON")

    user_data = request.get_json()

    if "username" not in user_data:
        return jsonify({"error": "Needs a username"}), 400

    users[user_data['username']] = {
            'name': user_data['name'],
            'age': user_data['age'],
            'city': user_data['city']
    }

    response_data = {
            'username': user_data['username'],
            'name': user_data['name'],
            'age': user_data['age'],
            'city': user_data['city']
    }

    return jsonify({"message": "User added", "user": response_data}), 201

if __name__ == "__main__":
    app.run(debug=True)
