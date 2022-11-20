
from flask import Blueprint, request
from app.models import db, Transaction, Account
from flask_login import current_user, login_required
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

# Blueprint
transaction_routes = Blueprint('transactions', __name__)

# Route
@transaction_routes.route('/')

# Login Required
@login_required

# The route function
def get_all_transactions():
    transactions = Transaction.query.join(Account).filter(Account.user_id == current_user.get_id()).order_by(Transaction.transaction_date.desc()).all()
    return {"transactions": [transaction.to_dict() for transaction in transactions]}

 # Route
@transaction_routes.route('/', methods=['POST'])
 # Login Required
@login_required
# The route function for adding a transaction
def add_transaction():
    # Get the data from the request body and store it in a variable 
    new_transaction = Transaction(
        transaction_date=request.json['transaction_date'],
        transaction_recipient=request.json['transaction_recipient'],
        transaction_amount=request.json['transaction_amount'],
        categoryId=request.json['categoryId'],
        accountId=request.json['accountId']
    )
    # Add the new transaction to the database
    db.session.add(new_transaction)
    # Commit the changes to the database
    db.session.commit()
    
    return new_transaction.to_dict()


# Route for deleting a transaction by id
@transaction_routes.route('/<int:transactionId>', methods=['DELETE'])
@login_required
def delete_transaction(transactionId):
    # get transaction by id
    transaction = Transaction.query.get(transactionId)
    # delete transaction
    db.session.delete(transaction)
    # commit changes
    db.session.commit()
    # return transaction as a dictionary
    return transaction.to_dict() 

# Route for updating a transaction by id
@transaction_routes.route('/<int:transactionId>', methods=['PUT'])
@login_required
def edit_transaction(transactionId):
    # get transaction by id
    transaction = Transaction.query.get(transactionId) 
    # update transaction with data from request body
    transaction.transaction_date = request.json['transaction_date']
    transaction.transaction_recipient = request.json['transaction_recipient']
    transaction.transaction_amount = request.json['transaction_amount']
    transaction.categoryId = request.json['categoryId']
    transaction.accountId = request.json['accountId']
    # commit changes
    db.session.commit()
    # return transaction as a dictionary
    return transaction.to_dict()



# This function gets all transactions in the database and returns them in a dictionary
@transaction_routes.route('/filter')
@login_required
def get_filtered_transactions():
     # get all transactions  in the database and store them in a variable  
    transactions = Transaction.query.join(Account).filter(Account.user_id == current_user.get_id()).order_by(Transaction.transaction_date.desc()).all()
    return {"transactions": [transaction.to_dict() for transaction in transactions]}

