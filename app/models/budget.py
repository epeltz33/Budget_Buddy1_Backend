from .db import db
from unicodedata import category # unicode category of a character


class Budget(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    budget_amount = db.Column(db.Float, nullable=False)
    budget_name = db.Column(db.String(50), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('User', back_populates='budgets') # one to many relationship with user model
    category = db.relationship('Category', back_populates='budgets') # this is the relationship to the category table