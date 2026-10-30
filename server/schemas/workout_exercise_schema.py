# workout exercise schema
from marshmallow import Schema, fields, post_load
from ..models import WorkoutExercise


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(allow_none=False)
    exercise_id = fields.Int(allow_none=False)
    reps = fields.Int(allow_none=False)
    sets = fields.Int(allow_none=False)
    duration_seconds = fields.Int()

    workout = fields.Nested("WorkoutSchema", exclude=("workout_exercises",))
    exercise = fields.Nested("ExerciseSchema", exclude=("workout_exercises",))

    @post_load
    def to_workout_exersise(self, data, **kwargs):
        return WorkoutExercise(**data)
