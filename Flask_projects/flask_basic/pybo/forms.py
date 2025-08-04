from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력하시오')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하시오')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하시오')])

class UserCreateForm(FlaskForm):
        username=StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
        password1 = PasswordField('비밀번호', validators=[
            DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
        password2 = PasswordField('비밀번호확인', validators=[DataRequired()])

        email = StringField('이메일', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])