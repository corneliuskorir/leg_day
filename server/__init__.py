from flask import Flask, make_response, request
from flask_migrate import Migrate
from .database import db


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
        return make_response({"message": "get workouts"}, 200)

    @app.route("/workouts", methods=["POST"])
    def create_workouts():
        data = request.get_json()
        return make_response({"message": "post workouts"}, 201)

    @app.route("/workouts/<id>", methods=["GET"])
    def get_workout(id):
        return make_response({"message": f"get workouts"}, 200)

    @app.route("/workouts/<id>", methods=["DELETE"])
    def delete_workout(id):
        return make_response({"message": f"get workouts"}, 204)

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
