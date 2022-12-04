from app.models import db, Budget


def seed_budgets(
):  # this is the function that will seed the budgets for the database and the budgets table
    shopping = Budget(budget_name='Shopping',
                      userId=1,
                      budget_amount=1000,
                      categoryId=19)
    dining = Budget(budget_name='Dining',
                    userId=1,
                    budget_amount=1000,
                    categoryId=6)
    total = Budget(budget_name='Total',
                   budget_amount=2500,
                   categoryId=1,
                   userId=1)
    groceries = Budget(budget_name='Groceries',
                       userId=1,
                       budget_amount=1000,
                       categoryId=13)

    db.session.add(shopping)
    db.session.add(dining)
    db.session.add(total)
    db.session.add(groceries)

    db.session.commit()


def undo_budgets():
    db.session.execute('TRUNCATE budgets RESTART IDENTITY CASCADE;')
    db.session.commit()
