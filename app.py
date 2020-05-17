import os
from src.api import create_app

def run():
    config_name = os.getenv('APP_SETTINGS') # config_name = "development"
    app = create_app(config_name)
    # method to run the flask app
    if __name__ == '__main__':
        app.run()