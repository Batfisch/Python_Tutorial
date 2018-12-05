from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user ={'username':'Patrick'}
    posts =[
        {
            'author': {'username':'Max'},
            'body': 'Heute ist Dienstag'
        },
        {
            'author': {'username': 'Peter'},
            'body': 'Morgen ist Mittwoch'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login from User: {}, Remember me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign up', form=form)
