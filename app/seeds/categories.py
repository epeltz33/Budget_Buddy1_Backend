from app.models import db, Category

def seed_categories():
  all = Category(category_name='All') # 1
  auto = Category(category_name='Auto & Transport') # 2
  bills = Category(category_name='Bills') # 3
  cash = Category(category_name='Cash & ATM') # 4
  charity = Category(category_name='Charity & Donations') # 5
  dining = Category(category_name='Dining & Drinks') # 6
  education = Category(category_name='Education') # 7
  entertainment = Category(category_name='Entertainment') # 8
  fees = Category(category_name='Fees & Charges') # 9
  financial = Category(category_name='Financial') # 10
  fitness = Category(category_name='Fitness') # 11
  gifts = Category(category_name='Gift') # 12
  groceries = Category(category_name='Groceries') # 13
  health = Category(category_name='Health') # 14
  home = Category(category_name='Home') # 15
  kids = Category(category_name='Kids') # 16
  personal = Category(category_name='Personal') # 17
  pets = Category(category_name='Pets') # 18
  shopping = Category(category_name='Shopping') # 19
  taxes = Category(category_name='Taxes') # 20
  travel = Category(category_name='Travel') # 21
  uncategorized = Category(category_name='Uncategorized') # 22

  db.session.add(all)
  db.session.add(auto)
  db.session.add(bills)
  db.session.add(cash)
  db.session.add(charity)
  db.session.add(dining)
  db.session.add(education)
  db.session.add(entertainment)
  db.session.add(fees)
  db.session.add(financial)
  db.session.add(fitness)
  db.session.add(gifts)
  db.session.add(groceries)
  db.session.add(health)
  db.session.add(home)
  db.session.add(kids)
  db.session.add(personal)
  db.session.add(pets)
  db.session.add(shopping)
  db.session.add(taxes)
  db.session.add(travel)
  db.session.add(uncategorized)
  
  db.session.commit()

def undo_categories():
  db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
  db.session.commit()
