from flask import Blueprint, jsonify, request, session
from app.models import User, db
from app.forms import LoginForm
from app.forms import  SignUpForm
from flask_login import login_user, logout_user, current_user, login_required
from datetime import date


# for backwards compatibility with flask-login
auth_routes = Blueprint('auth', __name__)


# function that will take WTForms validation errors and return them as a list
  
def WTForms_errors_to_list(validation_errors):
    errors = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errors.append(f'{field} : {error}')
    return errors

# auth_route decorator function for checking if user is authenticated
  
@auth_routes.route('/')
def authenticate():
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}, 401



@auth_routes.route('/login', methods=['POST'])
def login():
     """
        Login user
     """
     
     form = LoginForm()
    # retrieve csrf_token from request cookie and add it to the form 
     form.csrf_token = request.cookies.get('csrf_token')
     if form.validate_on_submit():
         user = User.query.filter(User.email == form.data['email']).first()
         login_user(user)
         return user.to_dict()
     else:
       return {'error': WTForms_errors_to_list(form.errors)}, 401

@auth_routes.route('/logout')
def logout():
    logout_user()
    return {'message': 'User has logged out'}

@auth_routes.route('/register', methods=['POST'])
def register():
    """
        Register user
    """
    form = SignUpForm()
    form.csrf_token = request.cookies.get('csrf_token')
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user) # session is a collection of objects that write to the database
        db.session.commit() 
        login_user(user) # login user after registering
        
        return user.to_dict()
    return {'error': WTForms_errors_to_list(form.errors)}, 401


@auth_routes.route('/unauthenticated')
def unauthenticated():
    return {'errors': ['Unauthorized']}, 401
