from app import applicaton
from flask import render_template


@applicaton.route('/')
@applicaton.route('/index')
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

