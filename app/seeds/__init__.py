from flask.cli import AppGroup
from .users import seed_users, undo_users

seeder = AppGroup('seed')

@seeder.command('all')
def seed():
	seed_users()

@seeder.command('undo')
def undo():
	undo_users()
