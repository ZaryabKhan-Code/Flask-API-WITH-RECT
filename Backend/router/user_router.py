from flask import Blueprint, jsonify, request
from util.user_util import *
import bcrypt

user_router = Blueprint('user', __name__)

@user_router.route('/api/register', methods=['POST'])
def register_user():
    """
    Register a new user
    ---
    tags:
      - User Credentials
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: The username of the new user
      - name: email
        in: formData
        type: string
        required: true
        description: The email address of the new user
      - name: password
        in: formData
        type: string
        required: true
        description: The password of the new user
    consumes:
      - application/x-www-form-urlencoded
    responses:
      201:
        description: User created successfully
      400:
        description: Bad request
      500:
        description: Internal server error
    """
    try:
        data = request.get_json()
        name = data['username']
        email = data['email']
        password = data['password']
        existing_user = get_user_by_email(email)
        if existing_user:
            return jsonify({'message': 'Email is already taken'}), 400
        existing_user = get_user_by_name(name)
        if existing_user:
            return jsonify({'message': 'Username is already taken'}), 400
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        add_user(name=name, email=email, password=password_hash)
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': f'Error creating user: {str(e)}'}), 500
    

@user_router.route('/api/check-username/<name>')
def check_username(name):
    """
    Check if a username is available, and suggest a new one if it's not.
    ---
    tags:
      - User Credentials
    parameters:
      - name: username
        in: path
        type: string
        required: true
        description: The username to check
    responses:
      200:
        description: Success
        schema:
          type: object
          properties:
            exists:
              type: boolean
              description: Indicates whether the username exists
            suggested_username:
              type: string
              description: If the username already exists, this is a suggested alternative
      400:
        description: Bad request
      500:
        description: Internal server error
    """
    existing_user = get_user_by_name(name)
    if existing_user:
        return jsonify({'exists': True, 'suggested_username': suggest_username(name)})
    else:
        return jsonify({'exists': False})