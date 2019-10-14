from flask import render_template, flash, redirect, url_for
from myapp import app
from myapp.form import Login, RegisterForm
from myapp.models import User


@app.route('/')
@app.route('/home')
def home():

    name = 'Sai'
    title = 'Home'
    form = Login()

    return render_template('home.html', title=title, name=name, form=form)


@app.route('/register')
def register():

    title = 'Register'
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    first_name=form.first_name.data, last_name=form.last_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {form.first_name.data}!')
        return redirect(url_for('home'))
    return render_template('register.html', title=title, form=form)
