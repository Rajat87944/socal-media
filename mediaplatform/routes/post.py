from flask import Blueprint, request, jsonify
from extensions import db
from models.post import Post

posts_bp = Blueprint('update/post', __name__)

@posts_bp.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()
    content = data.get('content')

    post = Post.query.get_or_404(post_id)

    if not content:
        return jsonify({"message": "Content is required"}), 400

    post.content = content
    db.session.commit()

    return jsonify({"message": "Post updated successfully!"}), 200

# Don't forget to register your blueprint in your main app file (e.g., main.py)
