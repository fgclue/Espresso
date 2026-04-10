from flask import Blueprint, abort

item = Blueprint('item', __name__, url_prefix="/item")

@item.route('/hi')
def abc():
    return "HI"

"""
item:        get, patch, put, delete
user:        get, patch, put, delete
transaction: get, patch, put, delete
roles:       get, patch, put, delete
"""