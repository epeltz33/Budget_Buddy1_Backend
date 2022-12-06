from flask_login import current_user, login_required
from flask import Blueprint, request
from app.models import Budget, db

budget_routes = Blueprint('budgets', __name__)


@budget_routes.route('/')
#@login_required
def get_all_budgets():
 #return Budget.query.all()
    budgets = Budget.query.all()
    return {'all_budgets': [budget.to_dict() for budget in budgets]}


@budget_routes.route('/<int:budgetId>', methods=['PUT'])
#@login_required
def edit_budget(budgetId):
    budget = Budget.query.get(budgetId)
    budget.budget_amount = request.json['budget_amount']
    db.session.commit()

    return budget.to_dict()
