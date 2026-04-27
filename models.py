"""
Database models and SQLAlchemy instance for FitTrack Pro.
"""

from datetime import datetime, timezone

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """
    User account model for registered FitTrack Pro users.
    """

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password_hash = db.Column(db.String(256), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    def set_password(self, password):
        """
        Hash and store the user's password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check a plain-text password against the stored password hash.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        Return a readable representation of the user object.
        """
        return f"<User {self.username}>"