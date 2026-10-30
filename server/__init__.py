from flask import Flask, make_response, request
from flask_migrate import Migrate
from .database import db
from .models import *
from .schemas import *


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["DEBUG"] = True

    # add migrations

    migrate = Migrate(app, db)

    db.init_app(app)

    @app.route("/")
    def home():
        return make_response({"message": "Welcome to Leg day fitness planner."}, 200)

    # workouts
    @app.route("/workouts", methods=["GET"])
    def get_workouts():
        workouts = Workout.query.all()
        if workouts:
            res = WorkoutSchema(many=True).dumps(workouts)
            return make_response(res, 200)

        return make_response({"error": "We cant find any workouts."}, 404)

    @app.route("/workouts", methods=["POST"])
    def create_workouts():
        try:
            data = request.get_json()
            workout = WorkoutSchema().load(data)
            db.session.add(workout)
            db.session.commit()
            return make_response({"message": "Workout created successfully"}, 201)
        except Exception as e:
            return make_response({"error": f"Failed to create workout: {e}"})

    @app.route("/workouts/<id>", methods=["GET"])
    def get_workout(id):
        workout = Workout.query.filter_by(id=id).first()
        if workout is not None:
            res = WorkoutSchema().dumps(workout)
            return make_response(res, 200)
        return make_response({"error": f"Failed to find workout: id[{id}]"}, 404)

    @app.route("/workouts/<id>", methods=["DELETE"])
    def delete_workout(id):
        try:
            workout = Workout.query.filter_by(id=id).first()
            if workout is not None:
                db.session.delete(workout)
                db.session.commit()
                return make_response({"message": f"Workout '{id}' deleted."}, 204)
            raise Exception("Workout not found")
        except Exception as e:
            return make_response({"error": f"Failed to delete workout: {e}"}, 404)

    # exercises
    @app.route("/exercises", methods=["GET"])
    def get_exercises():
        exercises = Exercise.query.all()
        if exercises:
            res = ExerciseSchema(many=True).dumps(exercises)
            return make_response(res, 200)

        return make_response({"error": "We cant find any Exercises."}, 404)

    @app.route("/exercises", methods=["POST"])
    def create_exercises():
        try:
            data = request.get_json()
            exercise = ExerciseSchema().load(data)
            db.session.add(exercise)
            db.session.commit()
            return make_response({"message": "Exercise created successfully"}, 201)
        except Exception as e:
            return make_response({"error": f"Failed to create exercise: {e}"})

    @app.route("/exercises/<id>", methods=["GET"])
    def get_exercise(id):
        exercise = Exercise.query.filter_by(id=id).first()
        if exercise is not None:
            res = ExerciseSchema().dumps(exercise)
            return make_response(res, 200)
        return make_response({"error": f"Failed to find exercise: id[{id}]"}, 404)

    @app.route("/exercises/<id>", methods=["DELETE"])
    def delete_exercise(id):
        try:
            exercise = Exercise.query.filter_by(id=id).first()
            if exercise is not None:
                db.session.delete(exercise)
                db.session.commit()
                return make_response({"message": f"Workout '{id}' deleted."}, 204)
            raise Exception("Excersise not found")
        except Exception as e:
            return make_response({"error": f"Failed to delete exercise: {e}"}, 404)

    @app.route(
        "/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises",
        methods=["POST"],
    )
    def create_workout_exercises(workout_id, exercise_id):
        try:
            data = request.get_json() | {
                "workout_id": workout_id,
                "exercise_id": exercise_id,
            }
            we = WorkoutExerciseSchema().load(data)
            db.session.add(we)
            db.session.commit()
            return make_response(
                {
                    "message": f"Workout {workout_id} with exercise {exercise_id} created successfully"
                },
                201,
            )
        except Exception as e:
            return make_response({"error": f"Failed to create exercise: {e}"})

    return app
