from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력하시오')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하시오')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하시오')])
