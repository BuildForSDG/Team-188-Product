import unittest
from src.api import db
from src.api.models.user_model import User
from .base import BaseTestCase


class TestUserModel(BaseTestCase):

    def setUp(self):
        """Define test variables"""
        self.user = User(
            first_name = 'kelvin', 
            last_name = 'mwas',
            email = 'test@test.com',
            password = 'test'
        )

    def test_encode_auth_token(self):
        db.session.add(self.user)
        db.session.commit()
        auth_token = self.user.encode_auth_token(self.user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        db.session.add(self.user)
        db.session.commit()
        auth_token = self.user.encode_auth_token(self.user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)


if __name__ == '__main__':
    unittest.main()