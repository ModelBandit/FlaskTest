import os

BASE_DIR = os.path.dirname(__file__)
print("BASE_DIR: ", BASE_DIR)

SQLALCHEMY_DATABASE_URI = "oracle+cx_oracle://scott:tiger@localhost:1521/xe"
print("SQLALCHEMY_DATABASE_URI:", SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False