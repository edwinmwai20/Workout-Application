Fitness Tracker API
This is a Flask-based REST API for tracking workouts and exercises. It uses SQLAlchemy for database management and Marshmallow for object serialization.


Python 3.12

Pipenv (for managing the virtual environment)


--- Dependencies --
The project relies on the following core libraries:

Library	Purpose
Flask	Web framework to handle routing and requests.
Flask-SQLAlchemy	ORM to interact with the SQLite/PostgreSQL database.
Flask-Migrate	Handles database migrations and schema changes.
Flask-Marshmallow	Integrates Marshmallow with Flask for easy serialization.
Marshmallow-SQLAlchemy	Bridges SQLAlchemy models and Marshmallow schemas.

--- Setup and Installation
Follow these steps to get your development environment running:

1. Clone and Enter Project
Navigate to your project directory in your Ubuntu terminal:

Bash
cd ~/MoringaSchool/path-to-your-project
2. Install Dependencies
Use Pipenv to create a virtual environment and install the packages listed in your Pipfile:

Bash
pipenv install
3. Activate the Virtual Environment
Bash
pipenv shell
4. Database Initialization
Since you are using Flask-Migrate, you need to initialize the database and run the initial migrations to create workout.db:

Bash
export FLASK_APP=run.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Seed the Database
Run the seed script to populate the database with initial exercises and a sample workout:

Bash
python seed.py
-- Running the Application
To start the development server, run:

Bash
python run.py
The API will be available at http://127.0.0.1:5000.

-- API Endpoints
Workouts
GET /workouts - Retrieve all workouts.

GET /workouts/<id> - Get a specific workout including its exercises.

POST /workouts - Create a new workout.

DELETE /workouts/<id> - Remove a workout.

Exercises
GET /exercises - List all available exercises.

POST /exercises - Add a new exercise to the library.

--Workout Details
POST /workouts/<w_id>/exercises/<e_id>/workout_exercises - Add a specific exercise to a workout session (sets/reps).

--Troubleshooting
ModuleNotFoundError: Ensure you are inside the pipenv shell.

Database Locked: Close any external database viewers (like SQLite Browser) before running migrations.

_________________________________________________________
How to Use the Fitness Tracker API
This guide explains the step-by-step workflow to manage your workouts and exercises. Since this application uses a relational database, you must follow a specific order: Create the "ingredients" (Exercises) and the "container" (Workout) before you can link them together.

 Step-by-Step Operation
1. Create an Exercise
First, you need to populate your exercise library. You cannot add "Pushups" to a workout if "Pushups" don't exist in the database yet.

Endpoint: POST /exercises

JSON Body:

JSON
{
  "name": "Pushups",
  "category": "Strength",
  "equipment_needed": false
}
2. Create a Workout Session
Next, create the main workout entry. This acts as the log entry for a specific day.

Endpoint: POST /workouts

JSON Body:

JSON
{
  "date": "2026-04-25",
  "duration_minutes": 45,
  "notes": "Feeling strong today, focusing on chest."
}
Note: Your logic currently checks for a name or category key to prevent errors. Ensure your JSON only contains workout-related fields.

3. Link Exercise to Workout (The Association)
Now that you have a Workout ID (e.g., 1) and an Exercise ID (e.g., 1), you can log how many reps and sets you did for that specific exercise during that workout.

Endpoint: POST /workouts/1/exercises/1/workout_exercises

JSON Body:

JSON
{
  "reps": 15,
  "sets": 3,
  "duration_seconds": 60
}
4. View Your Progress
Finally, you can retrieve your workout to see everything linked together.

Endpoint: GET /workouts/1

Expected Result: You will see the workout details along with a nested list of workout_exercises.