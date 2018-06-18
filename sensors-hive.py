from backend import backend, db
from backend.models import User, Token


@backend.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Token': Token}
