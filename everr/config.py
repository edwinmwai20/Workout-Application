class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///workout.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Prod(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://user:pass@localhost/library"