from ..database import db
from sqlalchemy.ext.associationproxy import association_proxy
from .workout_exercises import WorkoutExercise


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String)

    workout_exercises = db.relationship("WorkoutExercise", back_populates="workout")
    exercises = association_proxy(
        "workout_exercises",
        "exercise",
        creator=lambda exercise_obj: WorkoutExercise(exercise=exercise_obj),
    )
