from flask import Blueprint, request
from app.models import db, Transaction, Account
from flask_login import current_user, login_required
from sqlalchemy import func

transaction_routes = Blueprint('transactions', __name__)


@transaction_routes.route('/')
#@login_required
def get_all_transactions():
    transactions = Transaction.query.join(Account)

    return {
        'all_transactions':
        [transaction.to_dict() for transaction in transactions]
    }  # This is a list of dictionaries


@transaction_routes.route('/', methods=['POST'])
#@login_required
def add_transaction():
    new_transaction = Transaction(trans_date=request.json['trans_date'],
                                  trans_payee=request.json['trans_payee'],
                                  trans_amount=request.json['trans_amount'],
                                  categoryId=request.json['category_id'],
                                  accountId=request.json['account_id'])
    db.session.add(new_transaction)
    db.session.commit()

    return new_transaction.to_dict()


@transaction_routes.route('/<int:transactionId>', methods=['DELETE'])
#@login_required
def delete_transaction(transactionId):
    transaction = Transaction.query.get(transactionId)
    db.session.delete(transaction)
    db.session.commit()

    return transaction.to_dict()


@transaction_routes.route('/<int:transactionId>', methods=['PUT'])
#@login_required
def edit_transaction(transactionId):
    transaction = Transaction.query.get(transactionId)
    transaction.trans_payee = request.json['trans_payee']
    transaction.trans_date = request.json['trans_date']
    transaction.trans_amount = request.json['trans_amount']
    transaction.categoryId = request.json['categoryId']
    transaction.accountId = request.json['accountId']

    db.session.commit()

    return transaction.to_dict()


@transaction_routes.route('/filter')
#@login_required
def filter_by_payee():
    payeeQuery = request.args.get('payee')
    transactions = Transaction.query.all()
    return {
        'payee_transactions':
        [transaction.to_dict() for transaction in transactions]
    }
