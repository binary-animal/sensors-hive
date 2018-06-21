from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


backend = Flask(__name__, static_url_path='/static')
backend.config.from_object(Config)
db = SQLAlchemy(backend)
migrate = Migrate(backend, db)
login = LoginManager(backend)
login.login_view = 'login'  # url_for() forredirect if not logined and trying access to private part

from backend import routes, models
