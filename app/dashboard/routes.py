import json
from . import dashboard_bp

from flask import render_template

@dashboard_bp.route("/")
def index():
    with open("../db/data.json") as f:
        data = json.load(f)
        headers = data.keys(f)

    return render_template("dashboard/index.html", header=headers, data=data)