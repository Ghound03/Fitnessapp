"""
Main Flask application for FitTrack Pro.
"""

from flask import Flask, render_template
from flask_login import LoginManager

from config import Config
from models import db, User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user by their ID for Flask-Login sessions.
    """
    return User.query.get(int(user_id))


def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "login"

    @app.route("/")
    def home():
        """
        Render the home page.
        """
        return render_template("home.html")

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)