from src.api import db


class Section(db.model):
    """ Modeling sections of an article """
    section_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    section_number = db.Column(db.Integer)
    media_url = db.Column(db.String(255), nullable=True)
    section_header = db.Column(db.String(255), nullable=True)
    section_content = db.Column(db.String(2000), nullable=False)
    # id of the article the section belongs to.
    article_id = db.Column(db.Integer, nullable=False)

    def __init__(self, section_number, media_url,
                 section_header, section_content, article_id):
        self.section_number = section_number
        self.media_url = media_url
        self.section_header = section_header
        self.section_content = section_content
        self.article_id = article_id

# TODO
# add relationships
