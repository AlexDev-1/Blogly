"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()
default_img = "https://banner2.cleanpng.com/20180714/fok/kisspng-computer-icons-question-mark-clip-art-profile-picture-icon-5b49de29708b76.026875621531567657461.jpg"


def check_table_exists(table_name, app):
    with app.app_context():
        inspector = inspect(db.engine)
        return table_name in inspector.get_table_names()

class User(db.Model):
    """Class for Table User & Functions"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    first_name = db.Column(db.Text,
                            nullable = False)
    last_name = db.Column(db.Text,
                           nullable = False)
    image_url = db.Column(db.Text,
                           nullable = False,
                           default = default_img)
    
    @property
    def full_name(self):
        """Return full name of user."""
        return f'{self.first_name} {self.last_name}'
    
def connect_db(app):
    """Connect to Database."""

    db.app = app
    db.init_app(app)