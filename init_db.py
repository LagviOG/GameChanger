from ext import app, db
from models import Game,User

with app.app_context():

    db.drop_all()
    db.create_all()

    admin_user=User(username="admin123", password="admin123", role="admin")
    admin_user.create()