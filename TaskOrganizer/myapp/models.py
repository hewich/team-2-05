from werkzeug.security import generate_password_hash, check_password_hash
from myapp import db
from flask_login import UserMixin
from myapp import login



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    first_name = db.Column(db.String(128), unique=True)
    last_name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(60), nullable=False)
    task = db.relationship('Task', backref = 'author', lazy = 'dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(300), unique=True, nullable=False)
    due_date = db.Column(db.String(64), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Task {}>'.format(self.task_name, self.description, self.due_date)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))