from .db import db
from datetime import datetime
from sqlalchemy import Index 

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    transaction_amount = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    transaction_recipient = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    account = db.relationship('Account', back_populates='transactions')
    category = db.relationship('Category', back_populates='transactions')
    
    def to_dict(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'transaction_amount': self.transaction_amount,
            'transaction_date': self.transaction_date,
            'transaction_recipient': self.transaction_recipient,
            'category_id': self.category_id,
        }
        
Index('transaction_index', Transaction.transaction_recipient, postgresql_using='hash') # hash is the index type 
         