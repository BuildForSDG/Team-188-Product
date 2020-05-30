import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Base configuration."""
    DEBUG = False
    CSRF_ENABLED = True
    BCRYPT_LOG_ROUNDS = 13
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(BaseConfig):
    """Development Configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class TestingConfig(BaseConfig):
    """Testing Configuration, with a separate test database."""
    TESTING = True
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = "postgresql://kmwangemi:@localhost/test_db"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    
class ProductionConfig(BaseConfig):
    """Production Configuration."""
    DEBUG = False
    TESTING = False
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

# app_config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
# }