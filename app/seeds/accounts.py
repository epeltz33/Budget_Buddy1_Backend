from app.models import db, Account


def seed_accounts(): # this is the function that will seed the accounts for the database and the accounts table 
    amex = Account(account_name='American Express', account_balance=10000.00, userId=1)
    chase = Account(account_name='Chase',  account_balance=20000.00, userId=1)
    wells = Account(account_name='Wells Fargo',  account_balance=30000.00, userId=1)
    
    db.session.add(amex) # this is the function that will add the accounts to the database session
    db.session.add(chase)
    db.session.add(wells)
     # db.session.commit() # this is the function that will commit the database session  
     
def undo_accounts(): # this is the function that will undo the accounts for the database and the accounts table
    db.session.execute('TRUNCATE accounts RESTART IDENTITY CASCADE;') # truncate the accounts table and restart the identity
    db.session.commit() # commit the database session 

    