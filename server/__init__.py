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
                return make_response(
                    {"message": f"Workout '{workout.name}' deleted."}, 204
                )
            raise Exception("Workout not found")
        except Exception as e:
            return make_response({"error": f"Failed to delete workout: {e}"}, 404)

    # exercises
    @app.route("/exercises", methods=["GET"])
    def get_exercises():
        return make_response({"message": "get exercises"}, 200)

    @app.route("/exercises", methods=["POST"])
    def create_exercises():
        data = request.get_json()
        return make_response({"message": "post exercises"}, 201)

    @app.route("/exercises/<id>", methods=["GET"])
    def get_exercise(id):
        return make_response({"message": f"get exercises"}, 200)

    @app.route("/exercises/<id>", methods=["DELETE"])
    def delete_exercise(id):
        return make_response({"message": f"get exercises"}, 204)

    @app.route(
        "/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises",
        methods=["POST"],
    )
    def create_workout_exercises(workout_id, exercise_id):
        data = request.get_json()
        return make_response({"message": "post workout exercises"}, 201)

    return app
