from .db import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)
    
    transactions = db.relationship('Transaction', back_populates='category', cascade='all, delete')
    budgets = db.relationship('Budget', back_populates='category', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'category_name': self.category_name,
        }