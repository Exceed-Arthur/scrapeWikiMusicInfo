from website import db
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User():
    @property
    def is_active(self):
        return True
    def get_id(self):
        try:
            return str(self.email)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None


    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
