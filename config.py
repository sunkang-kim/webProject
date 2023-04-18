import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybo.db'))
# 설정에 의해 SQLite 데이터베이스가 사용되고, 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db로 저장됨.

# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False