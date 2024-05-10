# app.py (main application file)
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///academic_system.db'
db = SQLAlchemy(app)

# Model definitions
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    # Add more student fields as needed

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    # Add more course fields as needed

# Route definitions
@app.route('/')
def index():
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('index.html', students=students, courses=courses)

# Add more routes for CRUD operations on students and courses

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)