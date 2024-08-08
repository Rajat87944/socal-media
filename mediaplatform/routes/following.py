from flask import Blueprint
from models.user import User


following_bp = Blueprint('following', __name__)

@following_bp.route('/<int:user_id>', methods=['GET'])
def get_following(user_id):
    User = User.query.get(user_id)
