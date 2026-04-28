from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from config import Config
from models import db, User, Workout

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user by ID for Flask-Login.
    """
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "login"

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))

        if request.method == "POST":
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")

            existing_user = User.query.filter(
                (User.username == username) | (User.email == email)
            ).first()

            if existing_user:
                flash("Username or email already exists.", "danger")
                return redirect(url_for("register"))

            user = User(username=username, email=email)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            flash("Account created successfully. Please log in.", "success")
            return redirect(url_for("login"))

        return render_template("register.html")

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("dashboard"))

        if request.method == "POST":
            email = request.form.get("email")
            password = request.form.get("password")

            user = User.query.filter_by(email=email).first()

            if user and user.check_password(password):
                login_user(user)
                flash("Logged in successfully.", "success")
                return redirect(url_for("dashboard"))

            flash("Invalid email or password.", "danger")
            return redirect(url_for("login"))

        return render_template("login.html")

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        flash("You have been logged out.", "info")
        return redirect(url_for("home"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        workouts = Workout.query.filter_by(user_id=current_user.id)\
            .order_by(Workout.workout_date.desc()).all()

        return render_template(
            "dashboard.html",
            workouts=workouts
        )

    @app.route("/workout/new", methods=["GET", "POST"])
    @login_required
    def add_workout():
        if request.method == "POST":
            workout = Workout(
                title=request.form.get("title"),
                workout_type=request.form.get("workout_type"),
                duration_minutes=int(request.form.get("duration")),
                calories_burned=int(request.form.get("calories")),
                notes=request.form.get("notes"),
                user_id=current_user.id
            )

            db.session.add(workout)
            db.session.commit()

            flash("Workout added successfully.", "success")
            return redirect(url_for("dashboard"))

        return render_template("add_workout.html")

    @app.route("/workout/<int:workout_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit_workout(workout_id):
        workout = Workout.query.get_or_404(workout_id)

        if workout.user_id != current_user.id:
            flash("Access denied.", "danger")
            return redirect(url_for("dashboard"))

        if request.method == "POST":
            workout.title = request.form.get("title")
            workout.workout_type = request.form.get("workout_type")
            workout.duration_minutes = int(request.form.get("duration"))
            workout.calories_burned = int(request.form.get("calories"))
            workout.notes = request.form.get("notes")

            db.session.commit()

            flash("Workout updated successfully.", "success")
            return redirect(url_for("dashboard"))

        return render_template(
            "edit_workout.html",
            workout=workout
        )

    @app.route("/workout/<int:workout_id>/delete", methods=["POST"])
    @login_required
    def delete_workout(workout_id):
        workout = Workout.query.get_or_404(workout_id)

        if workout.user_id != current_user.id:
            flash("Access denied.", "danger")
            return redirect(url_for("dashboard"))

        db.session.delete(workout)
        db.session.commit()

        flash("Workout deleted.", "info")
        return redirect(url_for("dashboard"))

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)