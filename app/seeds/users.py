from app.models import db, User


def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    blake = User(
        username='blake', email='blake@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')

    db.session.add(demo)
    db.session.add(blake)
    db.session.add(bobbie)

    db.session.commit()
    
    
def undo_users(): # this is the undo function for the seed function above  
    # this will delete all the rows in the users table
    # ex: 
	db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
	db.session.commit()

