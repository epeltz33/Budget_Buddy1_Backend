import os
from flask import Flask, render_template, request, redirect, session, url_for
from flask_login  import LoginManager 
from flask_cors import CORS 
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf


from .models import db, User
from .routes.auth_routes import auth_routes # import auth_routes blueprint 
from .routes.user_routes import user_routes

from .seeds import seed_commands

from .config import Config


app = Flask(__name__)

 
 # login manager config
login_manager = LoginManager(app) 
login_manager.login_view = 'auth.unauthorized' # redirects to this route if user is not logged in

@login_manager.user_loader #  tells the login manager how to load a user
def load_user(id):
    return User.query.get(int(id)) # returns an int of the user id


app.cli.add_command(seed_commands)  # adds seed commands
 
app.config.from_object(Config) # loads config from config.py
app.register_blueprint(auth_routes, url_prefix='/routes/auth') # registers auth routes
app.register_blueprint(user_routes, url_prefix='/routes/users') # registers user routes


db.init_app(app) # initializes the database

Migrate(app, db) # initializes the Migrate which is used for migrations of the database schema

CORS(app) # allows cross origin requests

# do i need this?
#  it is used to protect against cross-site request forgery (CSRF) 

csrf = CSRFProtect(app) 
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path): # this is the react root route that will be used to serve the react app
    if path == "favicon.ico":
        return app.send_static_file('favicon.ico') # registers the favicon 
    return app.send_static_file('index.html') # sends the index.html file 
    