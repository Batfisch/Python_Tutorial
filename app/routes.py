from app import app
from flask import render_template


@app.route('/')
@app.route('/index')

def index():
    user ={'username':'Patrick'}
    posts =[

        {
            'author': {'username':'Max'},
            'body' : 'Heute ist Dienstag'

        },
        {
            'author': {'username':'Peter'},
            'body': 'Morgen ist Mittwoch'


        }
    ]

    return render_template('index.html',title='Home', user=user, posts=posts)



