from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Horatio'}
    posts = [
        {
            'author': {'username': 'Wen Kin'},
            'body': 'Beautiful day in Singapore mate!'
        },
        {
            'author': {'username': 'Shaila'},
            'body': 'This is rly nerdy! :p'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)


@app.route('/news')
def news():
    return ("No news today!")

@app.route('/login', methods =['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form = form)

# The above code uses the template stored in index.html within the templates folder
# It then fills the blanks in the render_template argument with the dynamic flags
