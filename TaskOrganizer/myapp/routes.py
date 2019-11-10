from flask import render_template, flash, redirect, url_for, Markup
from werkzeug.urls import url_parse

from myapp import app
from myapp import db
from myapp.form import LoginForm, RegisterForm, TaskForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from myapp.models import User, Task


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():

    name = 'Sai'
    title = 'Home'
    form = LoginForm()

    return render_template('home.html', title=title, name=name, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/landing')
@login_required
def landing():
    title = 'Landing Page'
    return render_template('landing.html', title=title)


@app.route('/register', methods=['GET', 'POST'])
def register():

    title = 'Register | Task Organizer'
    form = RegisterForm()
    if form.validate_on_submit():
        users = User(username=form.username.data, email=form.email.data,
                     first_name=form.first_name.data, last_name=form.last_name.data)
        users.set_password(form.password.data)
        db.session.add(users)
        db.session.commit()

        #message = Markup()
        flash('Account Created!, {string(users.first_name)}')
        # print("Account!")
        return redirect(url_for('home'))
    return render_template('register.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    title = 'Login | Task Organizer'

    if current_user.is_authenticated:
        return redirect(url_for('landing'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('login')

        return redirect(next_page)

    return render_template('login.html', title=title, form=form)


#@app.route ('/')
#def ind():
   # tasks = Task.query.all()

  #  return render_template('add.html', tasks= tasks)
#
@app.route ('/add', methods = ['GET', 'POST'])
def add():

    title = 'Add | Task Organizer'

    # task = TaskForm(request.form)
    task = TaskForm()
    print('hefasdfasf')
    if task.validate_on_submit():

        tasks = Task(task_name=task.task_name.data, description=task.description.data, due_date=task.due_date.data)
        db.session.add(tasks)
        db.session.commit()
    return render_template('add.html', title="add task", form=task)
