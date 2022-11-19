from app.models import db, Category

def seed_categories():
    all = Category(category_name='All')
    utilities = Category(category_name='Utilities')
    food = Category(category_name='Food')
    entertainment = Category(category_name='Entertainment')
    transportation = Category(category_name='Transportation')
    db.session.add(all)
    db.session.add(utilities)
    db.session.add(food)
    db.session.add(entertainment)
    db.session.add(transportation)
    db.session.commit()
    
def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()