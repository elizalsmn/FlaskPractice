from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY']='09a2a2d2d78bcf4b11e6992173f316f8'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db' # the three '/' r relative local path
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3' # the three '/' r relative local path
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flblog import routes