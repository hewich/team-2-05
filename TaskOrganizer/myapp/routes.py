from flask import render_template, flash, redirect, url_for
from myapp import app
from myapp import db
from myapp.form import Login, RegisterForm
from myapp.models import User


@app.route('/')
@app.route('/home',methods=['GET', 'POST'])
def home():

    name = 'Sai'
    title = 'Home'
    form = Login()

    return render_template('home.html', title=title, name=name, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    title = 'Register'
    form = RegisterForm()
    if form.validate_on_submit():
        users = User(username=form.username.data, email=form.email.data,
                    first_name=form.first_name.data, last_name=form.last_name.data)
        users.set_password(form.password.data)
        db.session.add(users)
        db.session.commit()
        flash('Account created!')
        return redirect(url_for('home'))
    return render_template('register.html', title=title, form=form)
