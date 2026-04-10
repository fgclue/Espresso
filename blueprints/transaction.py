from flask import Blueprint, abort

transactions = Blueprint('transactions', __name__, url_prefix="/transactions")

@transactions.route('/hi')
def abc():
    return "HI"

"""
item:        get, patch, put, delete
user:        get, patch, put, delete
transaction: get, patch, put, delete
roles:       get, patch, put, delete
"""