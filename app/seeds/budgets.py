from app.models import db, Budget
from datetime import datetime

def seed_budgets():
  # use the data from transactions.py to seed the budgets table 
    # with the data from transactions.py
 Utilities = Budget(
    account_id=1, 
    budget_amount=300.00,
    budget_date=datetime(2021, 1, 1),
    categoryId=1,
    )
 Food = Budget(
    account_id=1,
    budget_amount=400.00,
    budget_date=datetime(2021, 1, 2),
    categoryId=2,
    )
 Entertainment = Budget(
    account_id=1,
    budget_amount=500.00,
    budget_date=datetime(2021, 7, 3),
    categoryId=3,
    )
 Transportation = Budget(
    account_id=1,
    budget_amount=600.00,
    budget_date=datetime(2021, 2, 4),
    categoryId=3,
    )
 
 db.session.add(Utilities)
 db.session.add(Food)
 db.session.add(Entertainment)
 db.session.add(Transportation)
 db.session.commit()