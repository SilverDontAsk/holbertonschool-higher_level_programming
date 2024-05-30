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

@app.route('/data', methods=['GET'])
def get_data():
    """
    returns a jsonified list of users
    """
    try:
        logging.debug(f"Users dictionary: {users}")
        if users:
            user_list = list(users.keys())
            logging.debug(f"User list: {user_list}")
            return jsonify(user_list)
        else:
            return jsonify({"message": "No users found"}), 200
    except Exception as e:
        logging.error(f"Error in /data route: {e}")
        return jsonify({"error": "An error occurred"}), 500

@app.route('/status', methods=['GET'])
def get_status():
    """
    gets the status of the API
    """
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """
    gets and jsonifies users
    """
    user_data = users.get(username)
    if user_data:
        formatted_data = {
                "username": username,
                "name": user_data["name"],
                "age":user_data["age"],
                "city": user_data["city"]
        }
        return jsonify(formatted_data)
    else:
        return "User Not Found", 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    adds users
    """
    if request.method == 'POST':
        user_data = request.get_json()
        if user_data:
            username = user_data.get('username')
            users[username] = user_data
            return jsonify({"message": "User added", "user": user_data}), 201
        else:
            return jsonify({"error", "Username is required"}), 400
    else:
        return jsonify({"error", "Invalid JSON data"}), 400

if __name__ == "__main__":
    app.run()
