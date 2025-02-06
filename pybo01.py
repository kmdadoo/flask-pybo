from flask import Flask
# 플라스크 애플리케이션을 생성하는 코드.
app = Flask(__name__) # __name__이라는 변수에는 "pybo" 라는 문자열이 담긴

@app.route('/') # URL과 플라스크 코드를 매핑하는 플라스크의 데코레이터 즉, / URL이 요청되면 플라스크는 hello_pybo 함수를 실행시킨다.
def hello_pybo():
    return 'Hello, Pybo!'