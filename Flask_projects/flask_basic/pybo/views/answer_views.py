from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect
from datetime import datetime
from ..forms import AnswerForm

from pybo import db
from pybo.models import Question, Answer
from pybo.views.auth_views import login_required



bp = Blueprint("answer", __name__, url_prefix='/answer')

@bp.route("/create/<int:question_id>", methods=('GET', 'POST'))
@login_required
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_detail.html', question=question, form=form)

# @bp.route('/detail/', methods=['GET', 'POST'])
# def indexAnswer():
#     targetNum = request.args.get("question_id", type=int)
#     answer_list = Answer.query.filter(Answer.question_id==targetNum).all()
#     return render_template('answer/answer_list.html', answer_list=answer_list)