from app import serialization as ma
from models import Exercise, Workout, WorkoutExercise
from marshmallow import fields, validate

class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True

    name = fields.String(required=True, validate=validate.Length(min=2))

class WorkoutExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        include_fk = True
    exercise = ma.Nested(ExerciseSchema, dump_only=True)

class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
    
    workout_exercises = ma.Nested(WorkoutExerciseSchema, many=True, dump_only=True)