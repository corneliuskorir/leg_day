from marshmallow import Schema, fields, post_load
from datetime import date
from ..models import Workout


class WorkoutSchema(Schema):

    id = fields.Int(dump_only=True)
    date = fields.Date(load_default=date.today().isoformat())
    duration_minutes = fields.Int(allow_none=True)
    notes = fields.String(allow_none=False)

    workout_exercises = fields.List(
        fields.Nested("WorkoutExerciseSchema", exclude=("workout", "exercise"))
    )
    exercises = fields.List(
        fields.Nested("ExerciseSchema", exclude=("workouts", "workout_exercises"))
    )

    @post_load
    def to_workout(self, data, **kwargs):
        return Workout(**data)
