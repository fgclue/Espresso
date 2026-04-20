from flask import Flask, render_template
from blueprints.user import user, role
from blueprints.transaction import transactions
from blueprints.item import item
from models import db
from decimal import *

getcontext().prec = 3

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

@app.route("/")
def show_routes():
    def get_prefix(rule):
        parts = rule.strip("/").split("/")
        return parts[0] if parts[0] else "(root)"

    rules = sorted(app.url_map.iter_rules(), key=lambda r: r.rule)
    
    METHOD_ORDER = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"]

    groups = {}
    for rule in rules:
        prefix = get_prefix(rule.rule)
        groups.setdefault(prefix, []).append({
            "path": rule.rule,
            "endpoint": rule.endpoint,
            "methods": sorted(
                (method for method in rule.methods if method),
                key=lambda method: METHOD_ORDER.index(method) if method in METHOD_ORDER else len(rule.methods)
            ),
        })

    return render_template('routes.html', groups=groups)

app.register_blueprint(user)
app.register_blueprint(transactions)
app.register_blueprint(item)
app.register_blueprint(role)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(port=3141, debug=True)