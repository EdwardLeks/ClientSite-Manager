from flask import Blueprint, request, jsonify
from app.models.website import Website
from app.database import db

website_bp = Blueprint("website", __name__)

# Get all websites
@website_bp.route("/websites", methods=["GET"])
def get_websites():
    websites = Website.query.all()
    return jsonify([website.to_dict() for website in websites])

# Add a new website
@website_bp.route("/websites", methods=["POST"])
def add_website():
    data = request.json
    new_website = Website(
        url=data.get("url"),
        client_name=data.get("client_name"),
        client_email=data.get("client_email"),
        notes=data.get("notes"),
    )
    db.session.add(new_website)
    db.session.commit()
    return jsonify(new_website.to_dict()), 201
