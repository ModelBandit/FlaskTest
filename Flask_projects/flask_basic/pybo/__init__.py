from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import oracledb
lib_dir = r"C:\instantclient-basic-windows.x64-19.27.0.0.0dbru\instantclient_19_27"
import config
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    oracledb.init_oracle_client(lib_dir=lib_dir)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app


