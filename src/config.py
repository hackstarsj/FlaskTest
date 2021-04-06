import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = "MYSecretKEYHash"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////db.sqlite"
    JWT_SECRET_KEY = "MYSecretKEYHash"

app_config = {
    'development': Development,
    'production': Production,
}

CURRENT_ENV="development"
JWT_SECRET_KEY="MYSecretKEYHash"