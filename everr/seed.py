from app import create_app, db
from models import Exercise, Workout, WorkoutExercise
from datetime import datetime

app = create_app()

with app.app_context():
    print("Forcing table creation...")
    db.create_all() 
    

    print("Clearing old data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    pushups = Exercise(name="Pushups", category="Strength", equipment_needed=False)
    plank = Exercise(name="Plank", category="Core", equipment_needed=False)
    
    db.session.add_all([pushups, plank])
    db.session.commit()

    print("Seeding workout...")

    w1 = Workout(date=datetime.now().date(), duration_minutes=30, notes="Great morning session")
    db.session.add(w1)
    db.session.commit()

    print("Creating join table record...")
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=pushups.id, reps=15, sets=3)
    db.session.add(we1)
    db.session.commit()

    print("Seeding complete!")