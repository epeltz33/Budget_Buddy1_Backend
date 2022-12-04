from flask_login import current_user, login_required
from flask import Blueprint, request
from app.models import Account, db


# Blueprint
account_routes = Blueprint('accounts', __name__) 

# Route
@account_routes.route('/')
# The route function
def get_all_accounts():
     accounts = Account.query.filter(Account.userId == current_user.get_id()).all()
     return {'all_accounts': [account.to_dict() for account in accounts]}


# Route
@account_routes.route('/', methods=['POST'])
def add_account():
  new_account = Account(account_name=request.json['account_name'], userId=current_user.get_id())
  db.session.add(new_account)
  db.session.commit()

  return new_account.to_dict()

@account_routes.route('/<int:accountId>',methods=['DELETE'])
@login_required
def delete_account(accountId):
  account = Account.query.get(accountId)
  db.session.delete(account)
  db.session.commit()

  return account.to_dict()





@account_routes.route('/<int:accountId>', methods=['PUT'])
@login_required
def edit_account(accountId):
  account=Account.query.get(accountId)
  account.account_name=request.json['account_name']
  db.session.commit()

  return account.to_dict()

