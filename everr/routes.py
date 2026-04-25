from flask import Blueprint, request, jsonify
from app import db
from models import Workout, Exercise, WorkoutExercise
from schemas import WorkoutSchema, ExerciseSchema, WorkoutExerciseSchema

api_bp = Blueprint('api', __name__)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)
we_schema = WorkoutExerciseSchema()



#routes
@api_bp.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify(workouts_schema.dump(Workout.query.all())), 200


@api_bp.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return jsonify(workout_schema.dump(workout)), 200


@api_bp.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json() # Define data FIRST
    
    if 'name' in data or 'category' in data:
        return {"error": "Workout category already exists"}, 400
    
    try:
        new_workout = workout_schema.load(data, session=db.session)
        db.session.add(new_workout)
        db.session.commit()
        return jsonify(workout_schema.dump(new_workout)), 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

@api_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return '', 204


@api_bp.route('/exercises', methods=['GET'])
def get_exercises():
    return jsonify(exercises_schema.dump(Exercise.query.all())), 200

@api_bp.route('/exercises/<int:id>', methods=['GET'])
def get_exercise_by_id(id):
    exercise = Exercise.query.get_or_404(id)
    return jsonify(exercise_schema.dump(exercise)), 200

@api_bp.route('/exercises', methods=['POST'])
def post_exercise():
    data = request.get_json()
    new_exercise = Exercise(**data)
    db.session.add(new_exercise)
    db.session.commit()
    return jsonify(exercise_schema.dump(new_exercise)), 201

@api_bp.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    db.session.delete(exercise)
    db.session.commit()
    return {}, 204




@api_bp.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    data = request.get_json() or {}
    
    new_we = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data.get('reps'),
        sets=data.get('sets'),
        duration_seconds=data.get('duration_seconds')
    )
    
    db.session.add(new_we)
    db.session.commit()
    return we_schema.jsonify(new_we), 201