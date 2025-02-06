import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소
# SQLite 데이터베이스가 사용. 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"