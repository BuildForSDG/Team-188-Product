from datetime import datetime

from src.api import db
#from src.api.models.user_model import User


class Article(db.model):
    """ model for storing articles """
    __tablename__="articles"

    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_title = db.Column(db.String(300), nullable=False)
    article_author = db.Column(db.Integer) #many to one relationship with User
    article_sections = db.Column(db.String) #one article may have many sections attached
    article_footer = db.Column( db.String ) #ending of the footer
    timestamp = db.Column(db.Date)

    def __init__(self, article_title, article_author, article_sections, article_footer):
        self.article_author = article_author
        self.article_title = article_title
        self.article_footer = article_title
        self.article_sections = article_sections
        self.timestamp = datetime.now()

    
#TODO 
#add relationships