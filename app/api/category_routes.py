from app.models import Category, db
from flask import Blueprint, request
from flask_login import current_user, login_required


# Blueprint
category_routes = Blueprint('categories', __name__)

# Route
@category_routes.route('/')
# Login Required
@login_required
# The route function for getting all categories for a user
def get_all_categories():
    categories = Category.query.filter(Category.user_id == current_user.get_id()).all()
    return {"categories": [category.to_dict() for category in categories]}