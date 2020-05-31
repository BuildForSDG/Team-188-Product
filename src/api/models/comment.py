from datetime import datetime

from src.api import db


class Comment(db.model):
    """modelling article comments"""
    comment_id = db.Column(db.Integer, primary_key=True , autoincrement=True)
    article_id = db.Column(db.Integer) #map to article being commented
    comment_body = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.Date)

    def __init__(self, article_id, comment_body):
        self.article_id = article_id
        self.comment_body = comment_body
        self.timestamp = datetime.now()

#TODO 
#add relationships