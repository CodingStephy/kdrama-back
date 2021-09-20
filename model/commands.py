import click
from flask.cli import with_appcontext

from flask_server import db
from .model import user, actor, show, link

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    
