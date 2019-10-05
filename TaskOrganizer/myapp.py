from flask import Flask
from flask import render_template
from form import Login
from form import RegisterForm

from flask_sqlalchemy import SQLAlchemy
# uncomment line below once you have created the
# TopCities class inside the form.py file


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.test'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


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
    return render_template('register.html', title=title, form=form)


if __name__ == '__main__':
    app.run(debug=True)
