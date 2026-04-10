from flask import Blueprint, abort
# manages roles and users
user = Blueprint('user', __name__, url_prefix="/user")

@user.route('/hi', methods=["POST", "GET"])
def abc():
    return "HI"


@user.route('/ba', methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
def bca():
    return "HI"

"""
item:        get, patch, put, delete
user:        get, patch, put, delete
transaction: get, patch, put, delete
roles:       get, patch, put, delete
"""