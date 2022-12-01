from flask import Blueprint, jsonify, request, session
from app.models import User, db,Budget, Account, Transaction
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import login_user, logout_user, current_user, login_required
from datetime import date


# for backwards compatibility with flask-login
auth_routes = Blueprint('auth', __name__)


# function that will take WTForms validation errors and return them as a list
  
def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that takes WTForms validation errors and turns them into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages

@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)

        account = Account(account_name='My First Account', userId=user.id)
        db.session.add(account)
        db.session.commit()

        dining_trans = Transaction(trans_date=date.today(), trans_payee='Restaurant', trans_amount=100.00, categoryId=6, accountId=account.id)
        groceries_trans = Transaction(trans_date=date.today(), trans_payee='Supermarket', trans_amount=50.00, categoryId=13, accountId=account.id)
        shopping_trans = Transaction(trans_date=date.today(), trans_payee='Store', trans_amount=100.00, categoryId=19, accountId=account.id)
        db.session.add(dining_trans)
        db.session.add(groceries_trans)
        db.session.add(shopping_trans)
        db.session.commit()

        total = Budget(budget_name='Total', budget_amount=2500, categoryId=1, userId=user.id)
        shopping = Budget(budget_name='Shopping', budget_amount=1000, categoryId=19, userId=user.id)
        groceries = Budget(budget_name='Groceries', budget_amount=500, categoryId=13, userId=user.id)
        dining = Budget(budget_name='Dining', budget_amount=1000, categoryId=6, userId=user.id)
        db.session.add(total)
        db.session.add(shopping)
        db.session.add(groceries)
        db.session.add(dining)
        db.session.commit()

        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
