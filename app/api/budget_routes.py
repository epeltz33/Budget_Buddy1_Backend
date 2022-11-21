from flask_login import current_user, login_required
from flask import Blueprint, request
from app.models import Budget, db

# Blueprint configuration for budget routes   
budget_routes = Blueprint('budgets', __name__)
# login required decorator
@login_required
# function for getting all budgets for a user
def get_all_budgets():
    budgets = Budget.query.filter(Budget.user_id == current_user.get_id()).all()
    return {"budgets": [budget.to_dict() for budget in budgets]}

#route for editing a budget by id
@budget_routes.route('/<int:budgetId>', methods=['PUT'])
@login_required
def edit_budget(budgetId):
    # get budget by id
    budget = Budget.query.get(budgetId)
    # update budget
    budget.budget_name = request.json['budget_name']
    budget.budget_amount = request.json['budget_amount']
    # commit changes
    db.session.commit()
    # return budget as a dictionary
    return budget.to_dict()

