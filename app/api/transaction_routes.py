from flask import Blueprint, request
from app.models import db, Transaction
from flask_login import current_user, login_required
from sqlalchemy import func


transaction_routes = Blueprint('transactions', __name__)



@transaction_routes.route('/')
@login_required
def all_transactions():
	transactions = Transaction.query.filter(Transaction.user_id == current_user.id).all()
	return {"transactions": [transaction.to_dict() for transaction in transactions]}
