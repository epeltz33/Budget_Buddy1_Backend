from sqlalchemy import PrimaryKeyConstraint
from .db import db


class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)  
    account_name = db.Column(db.String(50), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) 
#   

    user = db.relationship('User', back_populates='accounts')
    transactions = db.relationship('Transaction', back_populates='account', cascade='all, delete')

    def to_dict(self):
	    return {
			'id': self.id,
			'account_name': self.account_name,
			'userId': self.userId,

		}
