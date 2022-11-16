from flask.cli import AppGroup
from .users import seed_users, undo_users


# this will make a seed group to hold all the seed commands


seed_commands = AppGroup('seed')


# this is the seed command that will use the seed function I defined above

@seed_commands.command('all')
def seed():
    seed_users()
    # add more seed commands when I make more models


# this is the undo command that will use the undo function I defined above

@seed_commands.command('undo')
def undo():
    undo_users()
    # add more undo commands when I make more models
    # example usage: flask seed undo users  (this will undo the users table)
