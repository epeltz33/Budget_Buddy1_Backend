import os 
from flask import Flask
from flask_login  import LoginManager 
from flask_cors import CORS 
from flask_migrate import Migrate


from .models import db, User 
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes


from .seeds import seed_commands

from .config import Config

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'auth.unauthorized'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

app.cli.add_command(seed_commands)


app.config.from_object(Config) # this is the line that is causing the error to be displayed in the terminal

app.register_blueprint(user_routes, url_prefix='/api/users')
app.register_blueprint(auth_routes, url_prefix='/api/auth')


db.init_app(app)
Migrate(app, db)

CORS(app)


@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def react_root(path):
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
     
    

