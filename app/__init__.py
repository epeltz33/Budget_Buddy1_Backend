import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config

from .models import db, User 
from .api.user_routes import user_routes
from .api.auth_routes import auth_routes


from .seeds import seed_commands



app = Flask(__name__)



login = LoginManager(app)
login.login_view = 'auth.unauthorized'
 
app.config.from_object(Config) 
 
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

app.cli.add_command(seed_commands)




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
    app.run()
    

