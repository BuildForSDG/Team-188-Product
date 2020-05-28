from unittest import TestCase
from instance.config import app_config
from flask import current_app
from src.api import create_app


class TestDevelopmentConfig(TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name = "development")

    def test_app_is_development(self):
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] == "postgresql://localhost/product_db"
        )

class TestTestingConfig(TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name = "testing")

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['DEBUG'] is True)
        self.assertTrue(
            self.app.config['SQLALCHEMY_DATABASE_URI'] == "postgresql://localhost/test_db"
        )

class TestProductionConfig(TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name = "production")

    def test_app_is_production(self):
        self.assertTrue(self.app.config['DEBUG'] is False)

class TestStagingConfig(TestCase):
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name = "staging")

    def test_app_is_staging(self):
        self.assertTrue(self.app.config['DEBUG'] is True)


if __name__ == '__main__':
    unittest.main()
