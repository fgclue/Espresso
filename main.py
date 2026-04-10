from itertools import groupby
from flask import Flask, render_template_string
from blueprints.user import user
from blueprints.transaction import transactions
from blueprints.item import item

app = Flask(__name__)

@app.route("/")
def show_routes():
    def get_prefix(rule):
        parts = rule.strip("/").split("/")
        return parts[0] if parts[0] else "(root)"

    rules = sorted(app.url_map.iter_rules(), key=lambda r: r.rule)
    
    METHOD_ORDER = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    groups = {}
    for rule in rules:
        prefix = get_prefix(rule.rule)
        groups.setdefault(prefix, []).append({
            "path": rule.rule,
            "endpoint": rule.endpoint,
            "methods": sorted(
                (m for m in rule.methods if m not in ("HEAD", "OPTIONS")),
                key=lambda m: METHOD_ORDER.index(m) if m in METHOD_ORDER else 99
            ),
        })

    html = """
    <!doctype html>
    <html>
    <head>
      <title>Espresso Debug</title>
      <style>
        body { font-family: monospace; padding: 2rem; }
        h1 { font-size: 1.5rem; color: #888; text-transform: uppercase;
             letter-spacing: .1em; margin: 2rem 0 .5rem; border-bottom: 1px solid #333; padding-bottom: .3rem; }
        h2 { font-size: .85rem; color: #888; text-transform: uppercase;
             letter-spacing: .1em; margin: 2rem 0 .5rem; border-bottom: 1px solid #333; padding-bottom: .3rem; }
        footer { font-size: .85rem; color: #888; text-transform: uppercase;
             letter-spacing: .1em; margin: 2rem 0 .5rem; padding-bottom: .3rem; }
        .tree { list-style: none; padding: 0; margin: 0; }
        .tree li { display: flex; align-items: baseline; margin-bottom: 0.2rem }
        .path { color: #79c0ff; min-width: 260px; }
        .endpoint { color: #888; min-width: 180px; }
        .badge  { padding: .1rem .4rem; font-size: .75rem; font-weight: bold; }
        .GET    { background: #98c610; color: white; }
        .POST   { background: #1283c4; color: white; }
        .PUT    { background: #f68243; color: white; }
        .DELETE { background: #db654e; color: white; }
        .PATCH  { background: #13f8f8; color: black; }
      </style>
    </head>
    <body>
      <h1>Espresso Debug</h1>
      {% for prefix, routes in groups.items() %}
        <h2>/ {{ prefix }}</h2>
        <ul class="tree">
          {% for r in routes %}
          <li>
            <span class="path">{{ r.path }}</span>
            <span class="endpoint">{{ r.endpoint }}</span>
            <span>
              {% for m in r.methods %}
              <span class="badge {{ m }}">{{ m }}</span>
              {% endfor %}
            </span>
          </li>
          {% endfor %}
        </ul>
      {% endfor %}
      <br>
      <footer>© 2026 biitle.nl</footer>
    </body>
    </html>
    """
    return render_template_string(html, groups=groups)

app.register_blueprint(user)
app.register_blueprint(transactions)
app.register_blueprint(item)

app.run(port=1234, debug=True)