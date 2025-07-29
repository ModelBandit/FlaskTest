from flask import Blueprint, render_template, request
from pybo.models import Question, Answer

bp = Blueprint("main", __name__, url_prefix='/')

@bp.route("/hello")
def hello_pybo():
    return "hello, pybo!"

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/', methods=['GET', 'POST'])
def indexAnswer():
    targetNum = request.args.get("question_id", type=int)
    answer_list = Answer.query.filter(Answer.question_id==targetNum).all()
    return render_template('answer/answer_list.html', answer_list=answer_list)