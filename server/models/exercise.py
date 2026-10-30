from ..database import db
from sqlalchemy.ext.associationproxy import association_proxy
from .workout_exercises import WorkoutExercise


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise")
    workouts = association_proxy(
        "workout_exercises",
        "workout",
        creator=lambda workout_obj: WorkoutExercise(workout=workout_obj),
    )
