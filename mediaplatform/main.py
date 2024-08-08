# main.py
from flask import Flask
from config.config import Config
from extensions import db
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Use Config class here
    db.init_app(app)
    
    register_blueprints(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
