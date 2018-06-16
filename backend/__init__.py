from flask import Flask

backend = Flask(__name__)

from backend import routes
