from app.models import db, User


def seed_users(): # Create a new user instance
	user1 = User(
     username='Demo-lition', email='demo@example.com', password='password')
	user2 = User(
     username='Test', email='test@example.com', password='password')
	user3 = User(
     username='Test2', email='test2@example.com', password='password')

	# Add the new user instance to the database
	db.session.add(user1)
	db.session.add(user2)
	db.session.add(user3)

	# Commit the changes to the database
	db.session.commit()


def undo_users():
	# Remove all users
	db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
	db.session.commit()


