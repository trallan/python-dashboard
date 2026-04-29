from . import dashboard_bp

from flask import render_template

@dashboard_bp.route("/")
def index():
    return render_template("dashboard/index.html")