from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # 플라스크 애플리케이션을 생성하는 코드
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM(object relational mapping) - 파이썬 문법만으로 데이터베이스를 다룰수있음.
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # bp 객체 등록 - 블루프린트
    # .views 폴더 안에 각 페이지 view를 담당하는 .py를 블루프린트 객체로 등록
    from .views import main_views, question_views, answer_views   
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
