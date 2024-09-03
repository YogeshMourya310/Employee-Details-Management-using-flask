# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    office = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.String(20), nullable=False)
