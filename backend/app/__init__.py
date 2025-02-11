from flask import Flask
from flask_cors import CORS
from app.database import db

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object("app.config.Config")

    # Initialize extensions
    db.init_app(app)
    CORS(app)  # Allow frontend to access API

    # Register routes
    from app.routes.website_routes import website_bp
    app.register_blueprint(website_bp, url_prefix="/api")

    return app
