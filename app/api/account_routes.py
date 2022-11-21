from flask_login import current_user, login_required
from flask import Blueprint, request
from app.models import Account, db

# Blueprint
account_routes = Blueprint('accounts', __name__) 

# Route
@account_routes.route('/')
# Login Required
@login_required
# The route function
def get_all_accounts():
    accounts = Account.query.filter(Account.user_id == current_user.get_id()).all()
    return {"accounts": [account.to_dict() for account in accounts]}


# Route
@account_routes.route('/', methods=['POST'])
# Login Required
@login_required
# The route function for adding an account
def add_account():
    # Get the data from the request body and store it in a variable 
    new_account = Account(
        account_name=request.json['account_name'],
        account_balance=request.json['account_balance'],
        userId=current_user.get_id()
    )
    # Add the new account to the database
    db.session.add(new_account)
    # Commit the changes to the database
    db.session.commit()
    
    return new_account.to_dict()

# Route for deleting an account by id
@account_routes.route('/<int:accountId>', methods=['DELETE'])
# Login Required
@login_required
def delete_account(accountId):
    # get account by id
    account = Account.query.get(accountId)
    # delete account
    db.session.delete(account)
    # commit changes
    db.session.commit()
    # return account as a dictionary
    return account.to_dict()

# Route for updating an account by id
@account_routes.route('/<int:accountId>', methods=['PUT'])
# Login Required
@login_required
def edit_account(accountId):
    # get account by id
    account = Account.query.get(accountId)
    # update account
    account.account_name = request.json['account_name']
    account.account_balance = request.json['account_balance']
    # commit changes
    db.session.commit()
    # return account as a dictionary
    return account.to_dict()