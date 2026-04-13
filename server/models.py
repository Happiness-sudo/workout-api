from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

# Exercise
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise')

# Workout
class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout')

# Join Table
class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    # simple validation
    @validates('sets')
    def validate_sets(self, key, value):
        if value is not None and value <= 0:
            raise ValueError("Sets must be greater than 0")
        return value