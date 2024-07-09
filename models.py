from flask_login import UserMixin
from ext import db, login_manager
from werkzeug.security import generate_password_hash



class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class Game(db.Model, BaseModel):

    __tablename__ = "games"

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    img = db.Column(db.String(), nullable = False)

class User(db.Model, BaseModel, UserMixin):

    __tablename__= "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable = False)
    password = db.Column(db.String(), nullable = False)
    role = db.Column(db.String(), nullable=False)

    def __init__(self, username, password, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.role = role


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)