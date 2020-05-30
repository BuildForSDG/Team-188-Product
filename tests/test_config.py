import unittest
from flask import current_app
from src.api import app


class TestDevelopmentConfig(unittest.TestCase):

    def create_app(self):
        app.config.from_object('instance.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == "postgresql://kmwangemi:123@localhost/product_db"
        )

class TestTestingConfig(unittest.TestCase):

    def create_app(self):
        app.config.from_object('instance.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == "postgresql://kmwangemi@localhost/test_db"
        )

class TestProductionConfig(unittest.TestCase):
    
    def create_app(self):
        app.config.from_object('instance.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
