# 블루프린트 임포트
# 라우팅 함수를 체계적으로 관리
# flask에서 URL과 함수의 매핑을 관리하기 위해 사용
from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return

@bp.route('/')
def index():
    return redirect(url_for('question._list'))