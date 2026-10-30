from datetime import date
from . import create_app
from .models import *
from .database import db

app = create_app()

with app.app_context():
    print("Initializing database seeding...")

    # 1. Clear the database tables in reverse order of dependencies
    # (Clearing WorkoutExercise first prevents foreign key constraint errors)
    print("Clearing existing data...")
    db.session.query(WorkoutExercise).delete()
    db.session.query(Workout).delete()
    db.session.query(Exercise).delete()
    db.session.commit()

    # 2. Add Exercises
    print("Creating sample exercises...")
    pushup = Exercise(name="Push-up", category="Chest", equipment_needed=False)
    squat = Exercise(name="Bodyweight Squat", category="Legs", equipment_needed=False)
    bicep_curl = Exercise(
        name="Dumbbell Bicep Curl", category="Arms", equipment_needed=True
    )
    bench_press = Exercise(
        name="Barbell Bench Press", category="Chest", equipment_needed=True
    )

    db.session.add_all([pushup, squat, bicep_curl, bench_press])
    # Flush to generate IDs for the relationships below
    db.session.flush()

    # 3. Add Workouts
    print("Creating sample workouts...")
    upper_body_day = Workout(
        date=date(2026, 10, 28),
        duration_minutes=45,
        notes="Focused on upper body pushing movements. Felt strong.",
    )
    leg_day = Workout(
        date=date(2026, 10, 29),
        duration_minutes=30,
        notes="Quick lower body session before work.",
    )

    db.session.add_all([upper_body_day, leg_day])
    db.session.flush()

    # 4. Link them together via WorkoutExercise
    print("Mapping exercises to workouts...")
    join_records = [
        # Upper Body Day Exercises
        WorkoutExercise(
            workout=upper_body_day,
            exercise=bench_press,
            sets=4,
            reps=8,
            duration_seconds=0,
        ),
        WorkoutExercise(
            workout=upper_body_day, exercise=pushup, sets=3, reps=15, duration_seconds=0
        ),
        WorkoutExercise(
            workout=upper_body_day,
            exercise=bicep_curl,
            sets=3,
            reps=12,
            duration_seconds=0,
        ),
        # Leg Day Exercises
        WorkoutExercise(
            workout=leg_day, exercise=squat, sets=4, reps=20, duration_seconds=0
        ),
    ]

    db.session.add_all(join_records)

    # 5. Commit all changes to the database
    db.session.commit()
    print("Database successfully seeded!")
