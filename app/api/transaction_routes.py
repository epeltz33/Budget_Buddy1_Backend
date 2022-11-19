from flask import Blueprint, request
from app.models import db, Transaction, Account
from flask_login import current_user, login_required
from sqlalchemy import func


transaction_routes = Blueprint('transactions', __name__)

@transaction_routes.route('/')
@login_required # this is a decorator that will check if the user is logged in before running the function
def get_all_transactions():
    transactions = Transaction.query.join(Account).filter(Account.user_id == current_user.get_id()).order_by(Transaction.transaction_date.desc()).all()
    return {"transactions": [transaction.to_dict() for transaction in transactions]} # this is a list comprehension that will return a list of dictionaries
# of all the transactions

@transaction_routes.route('/', methods=['POST'])
@login_required
def add_transaction():
    new_transaction = Transaction(transaction_date=request.json['transaction_date'], # this is the date of the transaction
      transaction_recipient=request.json['transaction_recipient'],
      transaction_amount=request.json['transaction_amount'],
      categoryId=request.json['categoryId'],
      accountId=request.json['accountId'])
    db.session.add(new_transaction)
    db.session.commit()
    
    return new_transaction.to_dict()

@transaction_routes.route('/<int:transactionId>', methods=['DELETE'])
@login_required
def delete_transaction(transactionId):
    transaction = Transaction.query.get(transactionId)
    db.session.delete(transaction)
    db.session.commit()
    return transaction.to_dict() 

@transaction_routes.route('/<int:transactionId>', methods=['PUT'])
@login_required
def edit_transaction(transactionId):
    transaction = Transaction.query.get(transactionId)
    transaction.transaction_date = request.json['transaction_date']
    transaction.transaction_recipient = request.json['transaction_recipient']
    transaction.transaction_amount = request.json['transaction_amount']
    transaction.categoryId = request.json['categoryId']
    transaction.accountId = request.json['accountId']
    db.session.commit()
    return transaction.to_dict()
 

