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

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # bp 객체 등록 - 블루프린트
    from .views import main_views   # .view 폴더[패키지] 안의 main_views 팡리
    app.register_blueprint(main_views.bp)

    return app
