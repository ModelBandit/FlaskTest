import os
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.dirname(__file__)
print("BASE_DIR: ", BASE_DIR)

SQLALCHEMY_DATABASE_URI = "oracle+oracledb://scott:tiger@localhost:1521/xe"
print("SQLALCHEMY_DATABASE_URI:", SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False