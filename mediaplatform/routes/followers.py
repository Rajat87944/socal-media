from flask import Blueprint, jsonify
from models.user import User

followers_bp = Blueprint('followers', __name__)

@followers_bp.route('/<int:user_id>', methods=['GET'])
def get_followers(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User not found!'}), 404

    # Get followers
    followers = [follower.username for follower in user.followers.all()]

    return jsonify({'followers': followers}), 200
