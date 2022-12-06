import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from .models import db, User, Account, Budget, Category, Transaction
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes
from .api.account_routes import account_routes
from .api.transaction_routes import transaction_routes
from .api.category_routes import category_routes
from .api.budget_routes import budget_routes

from .seeds import seed_commands

from .config import Config

app = Flask(__name__)




# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.login'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)
app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(account_routes, url_prefix='/api/accounts')
app.register_blueprint(transaction_routes, url_prefix='/api/transactions')
app.register_blueprint(category_routes, url_prefix='/api/categories')
app.register_blueprint(budget_routes, url_prefix='/api/budgets')


db.init_app(app)
Migrate(app, db)


# config CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type', 'Authorization', 'Access-Control-Allow-Credentials'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True 
app.config['CORS_EXPOSE_HEADERS'] = 'Access-Control-Allow-Origin: http://localhost:3000' 


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')


