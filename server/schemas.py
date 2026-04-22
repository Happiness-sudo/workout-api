from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

    @validates("name")
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("too short")


class WorkoutSchema(Schema):
    id = fields.Int()
    date = fields.Str(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError("invalid duration")


class WorkoutExerciseSchema(Schema):
    id = fields.Int()
    workout_id = fields.Int()
    exercise_id = fields.Int()
    reps = fields.Int()
    sets = fields.Int()
    duration_seconds = fields.Int()