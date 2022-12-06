from flask import Blueprint, request
from app.models import Account, db
from flask_login import current_user, login_required

account_routes = Blueprint('accounts', __name__)

@account_routes.route('/')
@login_required
def get_all_accounts():
  accounts = Account.query.filter(Account.userId == current_user.get_id()).all()
  return {'all_accounts': [account.to_dict() for account in accounts]}



@account_routes.route('/', methods=['POST'])
@login_required
def add_account():
  new_account = Account(account_name=request.json['account_name'], userId=current_user.get_id())
  db.session.add(new_account)
  db.session.commit()

  return new_account.to_dict()

# const data = { account_name: 'New Account' }

# fetch('/api/accounts/', {
#   method: 'POST',
#   headers: {
#     'Content-Type': 'application/json',
#   },
#   body: JSON.stringify(data),
# })
# .then(response => response.json())
# .then(data => {
#   console.log('Success:', data);
# })

@account_routes.route('/<int:accountId>',methods=['DELETE'])
@login_required
def delete_account(accountId):
  account = Account.query.get(accountId)
  db.session.delete(account)
  db.session.commit()

  return account.to_dict()

# fetch('/api/accounts/7', {method: 'Delete'}).then(res => res.json()).then(data => console.log(data));

@account_routes.route('/<int:accountId>', methods=['PUT'])
@login_required
def edit_account(accountId):
  account=Account.query.get(accountId)
  account.account_name=request.json['account_name']
  db.session.commit()

  return account.to_dict()

