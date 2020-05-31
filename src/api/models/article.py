from datetime import datetime

from src.api import db
# from src.api.models.user_model import User


class Article(db.Model):

    """ model for storing articles """

    __tablename__ = "articles"

    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_title = db.Column(db.String(255), nullable=False)
    # many to one relationship with User
    article_author = db.Column(db.Integer, db.ForeignKey('users.id'))
    # ending of the footerii
    article_footer = db.Column(db.String(255))
    timestamp = db.Column(
        db.DateTime, default=db.func.current_timestamp(), nullable=False)

    # sections
    sections = db.relationship("Section", backref="article", lazy=True)
    # comments
    comments = db.relationship("Comment", backref="article", lazy=True)

    def __init__(
        self, article_title,
        article_author, article_footer
    ):

        self.article_author = article_author
        self.article_title = article_title
        self.article_footer = article_title
        self.timestamp = datetime.now()


"""
TODO
add relationships
"""
