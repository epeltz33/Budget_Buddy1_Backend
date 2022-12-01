from app.models import db, Account


def seed_accounts(): # this is the function that will seed the accounts for the database and the accounts table 
    amex = Account(account_name='American Express', userId=1)
    chase = Account(account_name='Chase', userId=1)
    discover = Account(account_name='Discover', userId=1)
    capitalOne = Account(account_name='Capital One', userId=1)
    citi = Account(account_name='Citi', userId=1)
    
    db.session.add(amex)
    db.session.add(chase)
    db.session.add(discover)
    db.session.add(capitalOne)
    db.session.add(citi)
    
    db.session.commit()
    
def undo_accounts():
    db.session.execute('TRUNCATE accounts RESTART IDENTITY CASCADE;')
    db.session.commit()
    