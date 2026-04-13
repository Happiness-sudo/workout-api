from server.app import app
from server.models import db, Workout, Exercise

with app.app_context():
    db.drop_all()
    db.create_all()

    e1 = Exercise(name="Push Up", category="Strength", equipment_needed=False)
    e2 = Exercise(name="Running", category="Cardio", equipment_needed=False)

    w1 = Workout(date="2026-04-13", duration_minutes=30, notes="Morning workout")

    db.session.add_all([e1, e2, w1])
    db.session.commit()

    print("Database seeded!")