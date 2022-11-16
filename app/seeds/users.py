from app.models import db, User


def seed_users(): # Create a new user object 
	test1 = User(
      username='test1', email='test1@example.com', password='password')
	test2 = User(
	  username='test2', email='test2@example.com', password='password') 
	test3 = User(
       username='test3', email='test3@example.com', password='password')
	Eric = User( 
        username='theman34', email='theman34@example.com', password='password34')
 
	# Add the new user object to the database session
	db.session.add(test1)
	db.session.add(test2)	
	db.session.add(test3)
	db.session.add(Eric)
 
	# Commit the changes to the database
	db.session.commit()
 
def undo_users(): # Delete a user object
	db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;') # Restore the autoincrementing primary key sequence 
	db.session.commit()
 