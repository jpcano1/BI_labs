import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY", "cfiG7j1LOu")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT", "cfiG7j1LOu")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///" + os.path.abspath("example.db"))

class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLITE_DB = os.getenv("SQLITE_DB", "storage.db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(SQLITE_DB)

    SECRET_KEY = "cfiG7j1LOu"
    SECURITY_PASSWORD_SALT = "DukVKGDuJk"

class TestingConfig(Config):
    TESTING = True