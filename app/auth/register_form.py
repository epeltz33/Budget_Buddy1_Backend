from flask_wtf import FlaskForm
from sqlalchemy import String 
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    
    
def user_exists(form, field):
    print("Checking if user exists", field.data)
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError("Email provided already in use.")
    

def username_exists(form, field):
    print("Checking if username exists", field.data)
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError("Username provided already in use.")