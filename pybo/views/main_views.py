# 블루프린트 임포트
# 라우팅 함수를 체계적으로 관리
# flask에서 URL과 함수의 매핑을 관리하기 위해 사용
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'