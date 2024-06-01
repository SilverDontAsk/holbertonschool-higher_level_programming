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
    user_data = users.get(username)
    if user_data:
         response_data = {
            "username": user_data["username"],
            "name": user_data["name"],
            "age": user_data["age"],
            "city": user_data["city"]
        }
         response = json.dumps(response_data, indent=4)
         return Response(response, mimetype='application/json')
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    this thing adds users via curl in terminal so why the hell is it being marked as wrong
    it adds them well
    it gives the response on a user without a username AND
    it deals a duplicate username so i honestly have 0 to no idea
    """
    user_data = request.get_json()
    if not user_data or 'username' not in user_data or not user_data['username']:
        return jsonify({"message": "Missing username"}), 400
    required_fields = ['name', 'age', 'city']
    if any(field not in user_data or not user_data[field] for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    username = user_data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
            'username': username,
            'name': user_data['name'],
            'age': user_data['age'],
            'city': user_data['city']
    }

    response_data = {
        'message': 'User added',
        'user': {
            'username': users[username]['username'],
            'name': users[username]['name'],
            'age': users[username]['age'],
            'city': users[username]['city']
        }
    }

    response_json = (
        '{\n'
        '        "message": "User added",\n'
        '        "user": {\n'
        f'                "username": "{users[username]["username"]}",\n'
        f'                "name": "{users[username]["name"]}",\n'
        f'                "age": {users[username]["age"]},\n'
        f'                "city": "{users[username]["city"]}"\n'
        '        }\n'
        '}\n'
    )

    return Response(response_json, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)
