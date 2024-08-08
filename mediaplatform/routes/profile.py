from flask import Blueprint, request, jsonify
from models import user
from flask_jwt_extended import create_access_token
from extensions import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/create', methods=['POST'])
def create_profile():
    data = request.get_json()

    # Extract data from the request
    username = data.get('username')
    password_hash = data.get('password')
    email = data.get('email')
   

    # Check if all required fields are provided
    if not username or not password_hash or not email:
        return jsonify({"message": "Username, password, and email are required"}), 400

    # Check if the username already exists
    existing_user = user.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Username already exists"}), 400

    # Create a new user
    new_user = user(username=username, email=email)
    new_user.set_password(password_hash)  # Assuming you have a method to hash passwords
    db.session.add(new_user)
    db.session.commit()

    # Generate an access token
    access_token = create_access_token(identity=new_user.id)

    return jsonify({
        "message": "Profile created successfully",
        "access_token": access_token
    }), 201
