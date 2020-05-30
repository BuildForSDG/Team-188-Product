import unittest
from src.api import app, db


class BaseTestCase(unittest.TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.close()
        db.drop_all()
        db.create_all()