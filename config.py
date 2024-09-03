# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:{{secrets.sql_password}}@localhost:3306/<your_database>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
