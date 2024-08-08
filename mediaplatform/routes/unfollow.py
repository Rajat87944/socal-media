from flask import Blueprint, request, jsonify
from models.followers import Follower
from extensions import db

unfollow_bp = Blueprint('unfollow', __name__)

@unfollow_bp.route('/', methods=['DELETE'])
def unfollow():
    data = request.get_json()
    user_id = data.get('user_id')
    follower_id = data.get('follower_id')

    follow = Follower.query.filter_by(user_id=user_id, follower_id=follower_id).first()
    if follow:
        db.session.delete(follow)
        db.session.commit()
        return jsonify({'message': 'User unfollowed successfully!'}), 200
    return jsonify({'message': 'Follow relationship not found!'}), 404
