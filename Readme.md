# Leg Day Fitness Planner API

**Leg Day** is a Flask-based backend API designed to structure, track, and manage workouts and exercises. It provides a robust relational database mapping workouts to distinct exercises via schemas built for fast serialization.

## Features

- Uses `pipenv` for virtual environment isolation.
- Powered by Flask-SQLAlchemy with schema migrations via Flask-Migrate.
- Uses `marshmallow` for serialization and deserialization.

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy & Flask-Migrate
- Marshmallow
- SQLite

## Getting Started

### Prerequisites

Make sure you have **Python 3.x** and **pipenv** installed on your machine.

### Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com
cd leg-day
```

2. **Install dependencies**

```bash
pipenv install
```

3. **Activate the virtual environment**

```bash
pipenv shell
```

4. **Set up environment configurations**
   Navigate to your server directory and set the Flask application variable:

```bash
cd server
export FLASK_APP=.
```

_(Note: For Windows PowerShell, use `$env:FLASK_APP="."`)_

5. **Initialize and run database migrations**

```bash
flask db init
flask db upgrade head
```

6. **Run the API server**

```bash
flask run
```

The local server will start up by default.

## API Endpoints

### Core Root

- `GET /` - Returns application welcome message

### Workouts

- `GET /workouts` - Fetch all available workouts
- `POST /workouts` - Create a new workout profile
- `GET /workouts/<id>` - Fetch a single workout by its unique ID
- `DELETE /workouts/<id>` - Remove a single workout profile

### Exercises

- `GET /exercises` - Fetch all available fitness exercises
- `POST /exercises` - Create a new exercise profile
- `GET /exercises/<id>` - Fetch a single exercise by its unique ID
- `DELETE /exercises/<id>` - Remove a single exercise profile

### Relationship Maps

- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` - Link an exercise to a specific workout schedule

## Testing the API

It is highly recommended to use **Postman**, **Insomnia**, or a similar API client to interact with this application ecosystem.

Ensure your payload headers include `"Content-Type: application/json"` for all `POST` configurations.
