from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)
    from app.admin import admin
    app.register_blueprint(admin)

    from flask import redirect

    @app.route("/")
    def home():
        return redirect("/admin")

    return app