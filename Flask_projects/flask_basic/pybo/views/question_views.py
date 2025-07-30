from flask import Blueprint, render_template, request, redirect, url_for
from pybo.models import Question, Answer
from ..forms import QuestionForm, AnswerForm
from datetime import datetime

from pybo import db

bp = Blueprint("question", __name__, url_prefix='/question')

@bp.route("/hello")
def hello_pybo():
    return "hello, pybo!"

@bp.route('/list')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():
        print("그런 아침, 그런 생각, POST")
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now()
        )
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('question/question_form.html', form=form)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    # answer_list = Answer.query.filter(Answer.question_id==question_id).all()
    return render_template('question/question_detail.html', question=question, form=form)
