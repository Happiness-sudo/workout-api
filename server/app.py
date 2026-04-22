from flask import Flask, request, jsonify
from flask_migrate import Migrate
from .models import db, Workout, Exercise, WorkoutExercise
from .schemas import WorkoutSchema, ExerciseSchema

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


@app.route('/')
def home():
    return {"message": "Workout API is running"}


@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return jsonify(workouts_schema.dump(workouts))


@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)
    return workout_schema.dump(workout)


@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()

    try:
        valid = workout_schema.load(data)
    except Exception as e:
        return {"error": str(e)}, 400

    workout = Workout(**valid)

    db.session.add(workout)
    db.session.commit()

    return workout_schema.dump(workout), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return {"message": "Workout deleted"}


@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return jsonify(exercises_schema.dump(exercises))


@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)
    return exercise_schema.dump(exercise)


@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()

    try:
        valid = exercise_schema.load(data)
    except Exception as e:
        return {"error": str(e)}, 400

    exercise = Exercise(**valid)

    db.session.add(exercise)
    db.session.commit()

    return exercise_schema.dump(exercise), 201


@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return {"message": "Exercise deleted"}


@app.route('/workouts/<int:w_id>/exercises/<int:e_id>/workout_exercises', methods=['POST'])
def add_exercise(w_id, e_id):
    data = request.get_json()

    link = WorkoutExercise(
        workout_id=w_id,
        exercise_id=e_id,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(link)
    db.session.commit()

    return {"message": "Exercise added"}, 201


if __name__ == '__main__':
    app.run(debug=True)