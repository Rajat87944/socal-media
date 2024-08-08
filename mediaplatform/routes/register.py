from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

register_bp = Blueprint('register', __name__)

@register_bp.route('/', methods=['POST'])
def register():
    from models.user import User, db  # Import here to avoid circular import

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201
