from datetime import datetime
from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), autoincrement=True, nullable=False)
    password = db.Column(db.String(20), autoincrement=True, nullable=False)
    phone = db.Column(db.String(11), autoincrement=True, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
