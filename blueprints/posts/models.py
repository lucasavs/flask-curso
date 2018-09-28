from ext.db import db


class Post(db.Model):
    __tablename__ = 'post'
    title = db.Column(db.Integer, primary_key=True)
    tile = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
