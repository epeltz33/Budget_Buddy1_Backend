
from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

user_routes = Blueprint('users', __name__) # Blueprint configuration for user routes


@user_routes.route('/') 
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}

@user_routes.route('/<int:id>') # <int:id> is a route parameter that will be passed when the user is logged in
@login_required
def user(id): # id is the route parameter that was passed from above 
    user = User.query.get(id)
    return user.to_dict()
