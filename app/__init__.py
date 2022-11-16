from flask import Flask, render_template, request, redirect, session 
from flask_login  import LoginManager 
from flask_cors import CORS 
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
import os

from .models import db, User
from .routes.auth_routes import auth_routes
from .routes.user_routes import user_routes

from .config import Config
from .seeds import seed_commands

app = Flask(__name__)

CORS(app) # allows cross origin requests
 # login manager config
login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = 'auth.unauthorized' # route that handles unauthorized access

@login_manager.user_loader #  tells the login manager how to load a user
def load_user(id):
    return User.query.get(int(id)) # returns an int of the user id

 
app.config.from_object(Config) # loads config from config.py
app.register_blueprint(auth_routes, url_prefix='/routes/auth') # registers auth routes
app.register_blueprint(user_routes, url_prefix='/routes/users') # registers user routes


app.cli.add_command(seed_commands) # adds seed commands


db.init_app(app) # initializes the database
Migrate(app, db) # initializes the Migrate which is used for migrations of the database schema

@app.before_request # runs before every request
def before_request():
      print( "you should see this before each request" )
      # runs before every request
      pass
  
@app.after_request # runs after every request
def insert_csrf_token(response):
        # runs after every request
        csrf_token = generate_csrf()
        response.set_cookie('csrf_token', 
        csrf_token,
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get('FLASK_ENV') == 'production' else None, # samesite is a cookie attribute that helps prevent CSRF attacks (very interesting)
        httponly=True)  
        return response 
    
@app.route('/', defaults={'path': ''}) # sets the default path to the root route
@app.route('/<path:path>') # sets the path to the route  that was passed in 
def react_root(path):
    if path == "favicon.ico":
        return app.send_static_file('favicon.ico') # sends the favicon.ico file to the browser
    return app.send_static_file('index.html') # sends the index.html file to the browser


      
    