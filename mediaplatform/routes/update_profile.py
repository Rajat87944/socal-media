# routes/update_profile.py
from flask import Blueprint, request, jsonify
from models.user import User
from extensions import db

update_profile_bp = Blueprint('update_profile', __name__)

@update_profile_bp.route('/<user_id>', methods=['PUT'])
def update_profile(user_id):
    
    data = request.get_json()
    user = User.query.get(user_id)
    print("in update fun", user)

    if user:
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully!'}), 200
    return jsonify({'message': 'User not found!'}), 404
