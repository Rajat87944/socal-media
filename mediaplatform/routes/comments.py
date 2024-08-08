from flask import Blueprint, request, jsonify
from models.comment import Comment
from extensions import db


comments_bp = Blueprint('comments', __name__)

@comments_bp.route('/', methods=['POST'])
def add_comment():
    data = request.get_json()
    content = data.get('content')
    user_id = data.get('user_id')
    post_id = data.get('post_id')

    new_comment = Comment(content=content, user_id=user_id, post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({'message': 'Comment added successfully!'}), 201
