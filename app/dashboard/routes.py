import json
from pathlib import Path
from . import dashboard_bp
from flask import render_template

base_dir = Path(__file__).parent
db_path = base_dir / "../db/data.json"

@dashboard_bp.route("/")
def index():
    with open(db_path) as f:
        data = json.load(f)

    return render_template("dashboard/index.html", headers=data[0].keys(), data=data)