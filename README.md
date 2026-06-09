# Fitnessapp

FitTrack Pro is a Flask web application designed to help users track workouts, monitor calories burned, and view progress statistics.

This project was created for the Databases assignment and demonstrates Flask integration with a database, CRUD logic, authentication, HTML, CSS, JavaScript, and deployment preparation.

## Features

- User registration and login
- Secure password hashing
- Add workouts
- View workouts
- Edit workouts
- Delete workouts
- Progress statistics
- JavaScript chart using Chart.js
- Responsive HTML and CSS design
- SQLite for local development
- PostgreSQL-ready configuration for Render

## Technologies Used

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLAlchemy
- PostgreSQL
- SQLite
- HTML
- CSS
- JavaScript
- Chart.js
- Gunicorn
- Render

## Project Structure

```text
fittrack-pro/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── Procfile
├── README.md
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_workout.html
│   ├── edit_workout.html
│   ├── progress.html
│   ├── about.html
│   └── contact.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── instance/
    └── db.sqlite3