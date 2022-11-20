from flask.cli import AppGroup
from .users import seed_users, undo_users, seed_transactions, undo_transactions, seed_budgets, undo_budgets, seed_accounts, undo_accounts, seed_categories, undo_categories


# this will make a seed group to hold all the seed commands


seed_commands = AppGroup('seed')


# this is the seed command that will use the seed function I defined above

@seed_commands.command('all')
def seed():
    seed_users()
    seed_accounts()
    seed_categories()
    seed_budgets()
    seed_transactions()
# this is the undo command that will use the undo function I defined above

@seed_commands.command('undo')
def undo():
    undo_users()
    undo_accounts()
    undo_categories()
    undo_budgets()
    undo_transactions() 