from app.models import db, User


def seed_users(): # Create a new user object 
	test11 = User(
      username='test1', email='test1@example.com', password='password')
	test22 = User(
	  username='test2', email='test2@example.com', password='password') 
	test33 = User(
       username='test3', email='test3@example.com', password='password')
	Erick = User( 
        username='theman34', email='theman34@example.com', password='password34')
 
	# Add the new user object to the database session
	db.session.add(test11)
	db.session.add(test22)	
	db.session.add(test33)
	db.session.add(Erick)
 
	# Commit the changes to the database
	db.session.commit()
 
def undo_users(): # Delete a user object
    # flask db:seed:undo users  
	db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;') # Restore the autoincrementing primary key sequence 
	db.session.commit()
 