from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False, unique=True)

    category = db.Column(db.String, nullable=False)

    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship(
        'WorkoutExercise',
        back_populates='exercise',
        cascade="all, delete"
    )

    @validates('name')
    def validate_name(self, key, value):
        if not value or len(value.strip()) < 2:
            raise ValueError("Exercise name must be at least 2 characters")
        return value.strip()


class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.String, nullable=False)

    duration_minutes = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        'WorkoutExercise',
        back_populates='workout',
        cascade="all, delete"
    )


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

    @validates('sets', 'reps', 'duration_seconds')
    def validate_positive_numbers(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} must be 0 or greater")
        return value