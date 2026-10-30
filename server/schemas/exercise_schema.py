# Exercise schema
from marshmallow import Schema, fields, validate, validates, ValidationError


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=100))
    category = fields.String(required=True)
    equipment_needed = fields.Boolean(load_default=False)

    workout_exercises = fields.List(
        fields.Nested("WorkoutExerciseSchema", exclude=("exercise", "workout"))
    )

    workouts = fields.List(fields.Nested("WorkoutSchema", exclude=("exercises",)))

    @validates("category")
    def validates_category_type(self, value):
        allowed_categories = ["Chest", "Legs", "Arms", "Back", "Core"]
        if value not in allowed_categories:
            raise ValidationError(
                f"Category must be one of: {', '.join(allowed_categories)}"
            )
