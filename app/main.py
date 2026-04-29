from flask import Flask
from dashboard import dashboard_bp
from main import main_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

if __name__ == "__main__":
    app.run(debug=True)
