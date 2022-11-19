from app.models import db, Transaction
from datetime import datetime
 
def seed_transactions(): # this is the function that will seed the transactions table with data from the database and the transactions table   
    transaction1 = Transaction(
        account_id=1,
        transaction_amount=100.00,
        transaction_date=datetime(2021, 1, 1),
        transaction_recipient='Amazon',
        category_id=1,
    )
    transaction2 = Transaction(
        account_id=1,
        transaction_amount=200.00,
        transaction_date=datetime(2021, 1, 2),
        transaction_recipient='Target',
        category_id=2,
    )
    transaction3 = Transaction(
        account_id=1,
        transaction_amount=300.00,
        transaction_date=datetime(2021, 7, 3),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction4 = Transaction(
        account_id=1,
        transaction_amount=400.00,
        transaction_date=datetime(2021, 2, 4),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction5 = Transaction(
        account_id=1,
        transaction_amount=500.00,
        transaction_date=datetime(2021, 3, 5),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction6 = Transaction(
        account_id=1,
        transaction_amount=600.00,
        transaction_date=datetime(2021, 1, 6),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction7 = Transaction(
        account_id=1,
        transaction_amount=700.00,
        transaction_date=datetime(2021, 1, 7),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction8 = Transaction(
        account_id=1,
        transaction_amount=800.00,
        transaction_date=datetime(2021, 1, 8),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction9 = Transaction(
        account_id=1,
        transaction_amount=900.00,
        transaction_date=datetime(2021, 1, 9),
        transaction_recipient='Walmart',
        category_id=3,
    )
    transaction10 = Transaction(
        account_id=1,
        transaction_amount=1000.00,
        transaction_date=datetime(2021, 1, 10),
        transaction_recipient='Walmart',
        category_id=3,
    )
    
    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.add(transaction3)
    db.session.add(transaction4)
    db.session.add(transaction5)
    db.session.add(transaction6)
    db.session.add(transaction7)
    db.session.add(transaction8)
    db.session.add(transaction9)
    db.session.add(transaction10)
    
    db.session.commit()
     
def undo_transactions(): # this is the function that will delete all the data from the transactions table
    db.session.execute('TRUNCATE transactions RESTART IDENTITY CASCADE;')
    db.session.commit()

# Path: app/seeds/users.py -- this is the file that will seed the users table with data from the database and the users table