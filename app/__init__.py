import os
from flask import Flask, render_template, request, redirect, session, jsonify
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db, User, Account, Transaction, Category, Budget

from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.budget_routes import budget_routes
from .api.transaction_routes import transaction_routes
from .api.category_routes import category_routes
from .api.account_routes import account_routes

from .seeds import seed_commands

from .config import Config

app = Flask(__name__)

# login manager configuration
login = LoginManager(app)
#login.init_app(app)
login.login_view = 'auth.unauthorized'
login.login_message = 'Please log in to access this page.'




@login.user_loader  # decorator for loading a user by id
def load_user(id):
    return User.query.get(int(id))


# seed commands configuration
app.cli.add_command(seed_commands)

# app configuration
app.config.from_object(Config)
# register blueprints for routes
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(account_routes, url_prefix='/api/accounts')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(budget_routes, url_prefix='/api/budgets')
app.register_blueprint(transaction_routes, url_prefix='/api/transactions')
app.register_blueprint(category_routes, url_prefix='/api/categories')

# database configuration
db.init_app(app)  # initialize database with app as argument
Migrate(app, db)  # initialize migration with app and database as arguments

# CORS configuration
CORS(app)
app.config[
    'CORS_HEADERS'] = 'Content-Type', 'Authorization', 'Access-Control-Allow-Origin'
app.config[
    'CORS_ORIGINS'] = '*', 'http://localhost:3000', 'http://localhost:5000'
app.config[
    'CORS_METHODS'] = 'GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')