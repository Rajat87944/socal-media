from flask import Blueprint, request, jsonify
from models.followers import Follower
from extensions import db

follow_bp = Blueprint('follow', __name__)

@follow_bp.route('/', methods=['POST'])
def follow():
    data = request.get_json()
    user_id = data.get('user_id')
    follower_id = data.get('follower_id')

    new_follow = Follower(user_id=user_id, follower_id=follower_id)
    db.session.add(new_follow)
    db.session.commit()

    return jsonify({'message': 'User followed successfully!'}), 200
