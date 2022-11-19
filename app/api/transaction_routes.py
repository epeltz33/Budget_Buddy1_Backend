from flask import Blueprint, request
from app.models import db, Transaction, Account
from flask_login import current_user, login_required
from sqlalchemy import func


transaction_routes = Blueprint('transactions', __name__)



@transaction_routes.route('/')
@login_required
def all_transactions():
 transactions = Transaction.query.join(Account).filter(
     Account.userId == current_user.get_id()).order_by(Transaction.trans_date.desc())

 return {'all_transactions': [transaction.to_dict() for transaction in transactions]}

@transaction_routes.route('/', methods=['POST'])
@login_required
def add_transaction():
    new_transaction = Transaction(trans_date=request.json['trans_date'],
      trans_payee=request.json['trans_payee'],
      trans_amount=request.json['trans_amount'],
      accountId=request.json['accountId'])
    db.session.add(new_transaction)
    db.session.commit()

    return new_transaction.to_dict() # return the new transaction

@transaction_routes.route('/<int:id>', methods=['DELETE'])
@login_required

def delete_transaction(id):
    transaction = Transaction.query.get(id)
    db.session.delete(transaction)
    db.session.commit()
    return transaction.to_dict()

