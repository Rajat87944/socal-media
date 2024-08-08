#routes\__init__.py

from flask import Blueprint
from .register import register_bp
from .message import message_bp
from .update_profile import update_profile_bp
from .follow import follow_bp
from .unfollow import unfollow_bp
from .comments import comments_bp
from .uncomments import uncomment_bp
from .followers import followers_bp
from .following import following_bp
from .profile import profile_bp

# List of all blueprints
blueprints = [
    (register_bp, '/api/register'),
    (message_bp, '/api/message'),
    (update_profile_bp, '/api/update_profile'),
    (follow_bp, '/api/follow'),
    (unfollow_bp, '/api/unfollow'),
    (comments_bp, '/api/comments'),
    (uncomment_bp, '/api/uncomment'),
    (followers_bp, '/api/followers'),
    (following_bp, '/api/following'),
    (profile_bp,   '/api/profile')
]

def register_blueprints(app):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
