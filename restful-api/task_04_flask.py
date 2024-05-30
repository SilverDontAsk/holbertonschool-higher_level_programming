#!/usr/bin/python3
"""
Simple API in python with flask
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

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
    if not users:
        return "No users found", 404
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """
    gets the status of the API
    """
    return "OK"

@app.route
def get_user(username):
    """
    gets and jsonifies users
    """
    user_data = users.get(username)
    if user_data:
        return jsonify(user_data)
    else:
        return "User Not Found", 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    """
    user_data = requests.get_json()
    if user_data:
        username = user_data.get('username')
        users[username] = user_data
        return jsonify({"message": "User added successfully",
                        "user": user_data), 201
    else:
        return "Invalid JSON data", 400

if __name__ == "__main__":
    app.run()
