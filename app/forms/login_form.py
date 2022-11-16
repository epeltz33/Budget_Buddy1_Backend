from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User


def user_exists(form, field):
    print("Checking if user exists", field.data)
    email = field.data
    user = User.query.filter(User.email == email).first()
    if not user:
        raise ValidationError("Email provided not found.")

def password_matches(form, field):
    print("Checking if password matches", field.data)
    password = field.data
    email = form.data['email']
    user = User.query.filter(User.email == email).first()
    if not user:
        raise ValidationError("User does not exist.")
    if not user.check_password(password):
        raise ValidationError("Password does not match.")
    
    class LoginForm(FlaskForm): # FlaskForm is a class from flask_wtf
        email = StringField('email', validators=[DataRequired(), user_exists])
        password = StringField('password', validators=[DataRequired(), password_matches])

