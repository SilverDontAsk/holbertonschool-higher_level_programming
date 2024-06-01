#!/usr/bin/python3
"""
Simple API in python with flask
"""
from flask import Flask, jsonify, request, Response
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
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 400

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    this thing adds users via curl in terminal so why the hell is it being marked as wrong
    it adds them well
    it gives the response on a user without a username AND
    it deals a duplicate username so i honestly have 0 to no idea
    """
    data = request.get_json()
    if 'username' in data:
        username = data['username']
        users[username] = data
        return jsonify({"message": "User added", "user": data})
    else:
        return "Missing username in request", 400


if __name__ == "__main__":
    app.run(debug=True)
