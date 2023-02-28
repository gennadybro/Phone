from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Brogen'}
    posts = [ # список выдуманных постов
        {
            'author': {'nickname': 'Bro'},
            'body': 'Прекрасный день в Сыктывкаре'
        },
        {
            'author': {'nickname': 'Ivan'},
            'body': 'Это было здорово!'
        },
        {
            'author': {'nickname': 'Гена'},
            'body': 'Всё работает!'
        }
    ]

    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)
