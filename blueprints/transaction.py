from flask import Blueprint, abort

transactions = Blueprint('transactions', __name__, url_prefix="/transactions")

@transactions.route('/hi')
def abc():
    return "HI"

"""
item:        get, post, patch, delete
user:        get, post, patch, delete
transaction: get, post, patch, delete
roles:       get, post, patch, delete
"""