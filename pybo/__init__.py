from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    # 플라스크 애플리케이션을 생성하는 코드
    app = Flask(__name__)
    # app.config.from_object(config)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM(object relational mapping) - 파이썬 문법만으로 데이터베이스를 다룰수있음.
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # bp 객체 등록 - 블루프린트
    # .views 폴더 안에 각 페이지 view를 담당하는 .py를 블루프린트 객체로 등록
    from .views import main_views, question_views, answer_views, auth_views   
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
