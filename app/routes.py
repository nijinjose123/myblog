from app import application
from flask import render_template
from app.forms import LoginForm

@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Nijin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautful day is Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers ar so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@application.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

