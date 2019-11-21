from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_heroku import Heroku 

app = Flask(__name__)
app.config.from_object(Config)
heroku = Heroku(app)
db = SQLAlchemy(app)

login = LoginManager(app)
# right side is the function that's called to login users
login.login_view = 'login'

from myapp import routes, models
