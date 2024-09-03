# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:{{secrets.sql_password}}@localhost:3306/pythondb1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
