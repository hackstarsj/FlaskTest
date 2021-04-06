import os

from src.config import CURRENT_ENV
from src.app import create_app

if __name__ == '__main__':
    env_name =CURRENT_ENV
    app = create_app(env_name)
    # run app
    app.run()