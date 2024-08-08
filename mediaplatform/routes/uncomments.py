from flask import Blueprint, request, jsonify
from models.comment  import Comment
from extensions import db

uncomment_bp = Blueprint('uncomment', __name__)

@uncomment_bp.route('/', methods=['DELETE'])
def remove_comment():
    data = request.get_json()
    comment_id = data.get('comment_id')

    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return jsonify({'message': 'Comment removed successfully!'}), 200
    return jsonify({'message': 'Comment not found!'}), 404
