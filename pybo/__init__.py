from flask import Flask

def create_app():
    # 플라스크 애플리케이션을 생성하는 코드
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
