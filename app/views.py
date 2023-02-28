from flask import render_template
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Brogen'}
    posts = [ # список выдуманных постов
        {
            'author': {'nickname': 'Петров'},
            'body': 'т.р. 4061'
        },
        {
            'author': {'nickname': 'Иванов'},
            'body': 'т.р. 4062'
        },
        {
            'author': {'nickname': 'Сидоров'},
            'body': 'т.р. 4063'
        }
    ]

    return render_template("index.html",
                           title='Список',
                           user=user,
                           posts=posts)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)
