#Workoutapi

#Description

This project is a backend API built using Flask, SQLAlchemy, and Marshmallow. It is designed to help personal trainers track workouts and exercises.

The application allows users to create workouts, create exercises, and link exercises to workouts with additional details like sets, reps, and duration.

The goal of this project was to practice building a structured backend with relationships, validations, and RESTful routes.

#Tools used

Python
Flask
Flask SQLAlchemy
Flask Migrate
Marshmallow
SQLite

Installation

Clone the repository:

````bash
git clone https://github.com/Happiness-sudo/workout-api.git
cd workout-api


Install dependencies:

pipenv install
pipenv shell

Set the Flask app:

export FLASK_APP=server.app

Run migrations:

flask db upgrade

Seed the database:

python -m server.seed
Running the Application

Start the server:

flask run

You should see:

Running on http://127.0.0.1:5000/
API Endpoints
Workouts
GET /workouts
Returns all workouts
GET /workouts/<id>
Returns a single workout
POST /workouts
Creates a new workout
DELETE /workouts/<id>
Deletes a workout
Exercises
GET /exercises
Returns all exercises
GET /exercises/<id>
Returns a single exercise
POST /exercises
Creates a new exercise
DELETE /exercises/<id>
Deletes an exercise
Workout Exercises (Join Table)
POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises

Adds an exercise to a workout with reps, sets, or duration.

Notes
The project uses relationships to connect workouts and exercises.
Validations are included to prevent invalid data.
The database can be reset anytime using the seed file.
Author

Created as part of a backend development lab project.



Run:

```bash
git add README.md
git commit -m "Add README with project description and instructions"
````
