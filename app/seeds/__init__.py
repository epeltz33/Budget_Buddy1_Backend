from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .accounts import seed_accounts, undo_accounts
from .transactions import seed_transactions, undo_transactions
from .budgets import seed_budgets, undo_budgets



# this will make a seed group to hold all the seed commands


seed_commands = AppGroup('seed')

# how do I seed just one table?
# to seed one tables like budget, run: flask seed budget
# to seed all tables, run: flask seed all 

@seed_commands.command('all')
def seed():
    seed_users()
    seed_accounts()
    seed_categories()
    seed_budgets()
    seed_transactions()
# this is the undo command that will use the undo function I defined above
# to undo all the seed commands above, run: flask seed undo all
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_accounts()
    undo_categories()
    undo_budgets()
    undo_transactions() 
    
    