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
         response = json.dumps(response_data)
         return Response(response, mimetype='application/json')
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    """
    user_data = request.get_json()
    if not user_data or 'username' not in user_data or not user_data['username']:
        return jsonify({"message": "Missing username"}), 400
    required_fields = ['name', 'age', 'city']
    if any(field not in user_data or not user_data[field] for field in required_fields):
        return jsonify({"error": "Missing requires fields"}), 400

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
        'username': users[username]['username'],
        'name': users[username]['name'],
        'age': users[username]['age'],
        'city': users[username]['city']
    }

    response = json.dumps({"message": "User added", "user": response_data})
    return Response(response, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)
