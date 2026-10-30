from ..database import db
from sqlalchemy.ext.associationproxy import association_proxy
from .workout_exercises import WorkoutExercise
from sqlalchemy.orm import validates


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    @validates("name")
    def name_validation(self, value):
        if not value.strip() or len(value.strip()) < 1:
            raise ValueError("Invalid name, can not be empty.")
        unique = db.session.query(Exercise.id).filter_by(name=value).first()
        if unique is not None:
            raise ValueError("This name already exists.")

    workout_exercises = db.relationship("WorkoutExercise", back_populates="exercise")
    workouts = association_proxy(
        "workout_exercises",
        "workout",
        creator=lambda workout_obj: WorkoutExercise(workout=workout_obj),
    )
