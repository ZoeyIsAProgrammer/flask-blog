class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog.db"
    SECRET_KEY = "s4a863513s1acd1as3#@$55d6s"

class ProductionConfig(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    PORT = 8000

class TestingConfig(Config):
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True

