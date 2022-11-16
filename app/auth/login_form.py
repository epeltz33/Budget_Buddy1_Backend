from wtforms import StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class LoginForm(FlaskForm): 
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])


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
    

