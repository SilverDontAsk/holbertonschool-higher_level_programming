#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'silver'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
      "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
  }

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user.get('password'), password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        entrance_token = create_access_token(identity=username)
        return jsonify(entrance_token=entrance_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    c_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/admin-only')
@jwt_required()
def admin_only():
    c_user = get_jwt_identity()
    user_role = users.get(c_user, {}).get('role', '')
    if 'admin' in role:
        return jsonify(message="Admin Acess: Granted"), 200
    else:
        return jsonify({"msg": "Unathorized acess"}), 403

if __name__ == '__main__':
    app.run(debug=True)

