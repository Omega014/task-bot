import os

from flask import Flask, render_template, session, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user

from apps.models import User, Channel, Question
from apps.database import init_db


def create_app():
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config['SECRET_KEY'] = 'omega014'
    app.config.from_object('apps.config.Config')

    init_db(app)

    return app


app = create_app()


# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


def get_login_user():
    if "user_id" not in session:
        return None


@app.route("/")
def index():
    user = session.get('user_id')
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET'])
def form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    user = User()
    login_user(user)
    return redirect(url_for('mypage'))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_required
@app.route("/mypage")
def mypage():
    user = session.get('user_id')
    user_channel = User.query.get(user).user_channel
    return render_template('mypage.html', user=user, channel=user_channel)


@login_required
@app.route("/channel/<channel_id>")
def grourp(channel_id):
    channel = Channel.query.get(channel_id)
    questions = Question.query.filter_by(channel_id=channel.id).all()
    return render_template('channel.html', channel=channel, users=channel.users, questions=questions)


@login_required
@app.route("/channel/<channel_id>/question_edit")
def question_index(channel_id):
    channel = Channel.query.get(channel_id)
    return render_template('question/edit.html', channel=channel)


@login_manager.user_loader
def load_user(user_id):
        return User()
