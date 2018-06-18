import os
from typing import Any, Union, Optional

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-it-h4x0r'
    SQLALCHEMY_DATABASE_URI: Union[Optional[str], Any] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../sensorshive.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
