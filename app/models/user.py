from .db import db
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    
    accounts = db.relationship('Account', back_populates='user', cascade='all, delete') # one to many relationship with accounts
    budgets = db.relationship('Budget', back_populates='user', cascade='all, delete') # one to many relationship with budgets
    
    @property
    def password(self):
        return self.hashed_password
    
    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
        