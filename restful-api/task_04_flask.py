#!/usr/bin/python3
"""
Simple API in python with flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

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
    user_data = users.get(username)
    if user:
        return jsonify(user_data)
    else:
        return jsonify({"error": "User Not Found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    """
    n_user = request.json
    username = n_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
            "username": username,
            "name": n_user["name"],
            "age": n_user["age"],
            "city": n_user["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 200

if __name__ == "__main__":
    app.run()
