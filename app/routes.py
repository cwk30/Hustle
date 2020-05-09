from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect('/home')
    return render_template('index.html', title='Sign In', form=form)

@app.route('/home/')
def home():
    user = {'username': 'Miguel'}
    return render_template('home.html', title='Getting Started', user=user)
    

    
    