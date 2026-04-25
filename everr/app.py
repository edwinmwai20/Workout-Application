from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_migrate import Migrate

db = SQLAlchemy()
serialization = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    serialization.init_app(app)
    migrate.init_app(app, db)

    from models import Exercise, Workout, WorkoutExercise 

    from routes import api_bp
    app.register_blueprint(api_bp)

    return app