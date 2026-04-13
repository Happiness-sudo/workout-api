from flask import Flask, request, jsonify
from flask_migrate import Migrate
from .models import db, Workout, Exercise, WorkoutExercise

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return {"message": "Workout API is running"}

# ---------------- WORKOUTS ----------------

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()

    return jsonify([
        {
            "id": w.id,
            "date": w.date,
            "duration_minutes": w.duration_minutes,
            "notes": w.notes
        }
        for w in workouts
    ])


@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get_or_404(id)

    return jsonify({
        "id": workout.id,
        "date": workout.date,
        "duration_minutes": workout.duration_minutes,
        "notes": workout.notes
    })


@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()

    workout = Workout(
        date=data.get("date"),
        duration_minutes=data.get("duration_minutes"),
        notes=data.get("notes")
    )

    db.session.add(workout)
    db.session.commit()

    return jsonify({"message": "Workout created"}), 201


@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({"message": "Workout deleted"})

# ---------------- EXERCISES ----------------

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify([
        {
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "equipment_needed": e.equipment_needed
        }
        for e in exercises
    ])


@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    return jsonify({
        "id": exercise.id,
        "name": exercise.name,
        "category": exercise.category,
        "equipment_needed": exercise.equipment_needed
    })


@app.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()

    exercise = Exercise(
        name=data.get("name"),
        category=data.get("category"),
        equipment_needed=data.get("equipment_needed")
    )

    db.session.add(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise created"}), 201


@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({"message": "Exercise deleted"})

# ---------------- JOIN TABLE ----------------

@app.route('/workouts/<int:w_id>/exercises/<int:e_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(w_id, e_id):
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

    return jsonify({"message": "Exercise added to workout"}), 201


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    