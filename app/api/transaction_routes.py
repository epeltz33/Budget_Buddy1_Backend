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
    trans_payee = request.json['trans_payee'], # trans_payee is a string of the payee name
