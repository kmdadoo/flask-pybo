from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm): 
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')]) 
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')]) 

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm): # 계정 생성을 위한 폼
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    # EqualTo('password2') 는 password1과 password2의 값이 일치해야 함을 의미한다.
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    # Email() 검증조건은 해당 속성의 값이 이메일형식과 일치하는지를 검증
    email = EmailField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])