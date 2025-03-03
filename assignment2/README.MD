**ERD and Python API**
1.
        1. ![Alt text](/assignment2/images/CIDM_assignment_2.png)
        2. [Download the PDF](/assignment2/images/CIDM_assignment_2.pdf)

2. 
```
from fastapi import FastAPI

"""
We can use FastAPI to create a basic HTTP/RESTful API in Python.

assumes that the following packages have been installed useing pip:
1. pip install fastapi
2. pip install uvicorn

Or, we can use the built-in fastapi command to run the API, but we'll need an additional package installation:
1. pip install "fastapi[standard]"

Altnatively, you we can use fastapi diectly from the command line:
1. uvicorn fastAPI:app --reload

"""
app = FastAPI()


# root route
@app.get("/")
def read_root():
    return {"Welcom to SoundBody, please login!"}


@app.get("/api/greet/{musicianName}")
def greet(musicianName: str):
    return {"message": f"Welcome to SoundBody, {musicianName}!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
```
3.
```
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

"""
For this example, we'll use uvicorn to run the API:
1. uvicorn main3:app --reload
"""

app = FastAPI()

# brush up on Pydantic Models: https://docs.pydantic.dev/latest/


class Musician(BaseModel):
    musicianId: int
    name: str
    email: str
    instrument: str
    fitnessLevel: str


musicians  = {
    "1": Musician(musicianId="1", name="Peter", email="peter@drums.com", instrument="drums", fitnessLevel="Med-high"),
    "2": Musician(musicianId="2", name="Alex", email="Alex@guitar.com", instrument="guitar", fitnessLevel="Med-high"),
    "3": Musician(musicianId="3", name="Kyle", email="kyle@bass.com", instrument="bass", fitnessLevel="Med"),
    "4": Musician(musicianId="4", name="Pat", email="pat@keys.com", instrument="keys", fitnessLevel="Low")
}

class Trainer(BaseModel):
    trainerId: int
    name: str
    email: str
    expertise: str 
    certification: str

trainers  = {
    "5": Trainer(trainerId="5", name="Steve", email="steve@trainer.com", expertise="drums", certification="ACSM"),
    "6": Trainer(trainerId="6", name="John", email="john@trainer.com", expertise="guitar", certification="ACSM"),
    "7": Trainer(trainerId="7", name="Mark", email="mark@trainer.com", expertise="bass", certification="ACSM"),
    "8": Trainer(trainerId="8", name="Tyler", email="tyler@trainer.com", expertise="keys", certification="ACSM")
}

class Exercise(BaseModel):
    exerciseId: int
    name: str
    instructions: str 
    muscleGroup: str
    difficultyLevel: str

exercises  = {
    "9": Exercise(exerciseId="9", name="Overhead Press", instructions="Stand with feet shoulder-width apart, grip the barbell just outside shoulder width, brace your core, press the bar overhead by extending your arms fully while keeping it in line with your midfoot, lock out at the top, then lower the bar back to shoulder level with control.", muscleGroup="shoulders", difficultyLevel="Med"),
    "10": Exercise(exerciseId="10", name="Squat", instructions="Stand with feet shoulder-width apart, keep your chest up, engage your core, lower your body by bending your knees and pushing your hips back until your thighs are parallel to the floor, keep your knees aligned with your toes, then push through your heels to return to the starting position.", muscleGroup="Legs", difficultyLevel="High"),
    "11": Exercise(exerciseId="11", name="Deadlift", instructions="Stand with feet hip-width apart, grip the barbell with hands just outside your knees, keep your back straight and core engaged, hinge at your hips and lower the bar while keeping it close to your body, then drive through your heels, extending your hips and knees to lift the bar to a standing position, squeezing your glutes at the top before lowering it back down with control.", muscleGroup="Low back", difficultyLevel="High"),
    "12": Exercise(exerciseId="12", name="Bench Press", instructions="Lie flat on a bench, grip the bar slightly wider than shoulder-width, lower the bar to your chest, keeping elbows at a 45-degree angle, then push the bar back up to arm’s length, fully extending your arms..", muscleGroup="Chest", difficultyLevel="Low")
}




@app.get("/")
def read_root():
    return {"Welcome, please login!"}

# CRUD Routes for Musician
@app.post("/musicians/")
def create_musician(musician: Musician):
    musicians[musician.musicianId] = musician
    return {"message": "Musician created", "musician": musician}

@app.get("/musicians/{musicianId}")
def read_musician(musicianId: int):
    musician = musicians.get(musicianId)
    if musician:
        return {"musicianId": musicianId, "musician": musician}
    return {"message": "Musician not found"}

@app.put("/musicians/{musicianId}")
def update_musician(musicianId: int, updated_musician: Musician):
    if musicianId in musicians:
        musicians[musicianId] = updated_musician
        return {"message": "Musician updated", "musician": updated_musician}
    return {"message": "Musician not found"}

@app.delete("/musicians/{musicianId}")
def delete_musician(musicianId: int):
    if musicianId in musicians:
        del musicians[musicianId]
        return {"message": "Musician deleted"}
    return {"message": "Musician not found"}

# CRUD Routes for Trainer
@app.post("/trainers/")
def create_trainer(trainer: Trainer):
    trainers[trainer.trainerId] = trainer
    return {"message": "Trainer created", "trainer": trainer}

@app.get("/trainers/{trainerId}")
def read_trainer(trainerId: int):
    trainer = trainers.get(trainerId)
    if trainer:
        return {"trainerId": trainerId, "trainer": trainer}
    return {"message": "Trainer not found"}

@app.put("/trainers/{trainerId}")
def update_trainer(trainerId: int, updated_trainer: Trainer):
    if trainerId in trainers:
        trainers[trainerId] = updated_trainer
        return {"message": "Trainer updated", "trainer": updated_trainer}
    return {"message": "Trainer not found"}

@app.delete("/trainers/{trainerId}")
def delete_trainer(trainerId: int):
    if trainerId in trainers:
        del trainers[trainerId]
        return {"message": "Trainer deleted"}
    return {"message": "Trainer not found"}

# CRUD Routes for Exercise
@app.post("/exercises/")
def create_exercise(exercise: Exercise):
    exercises[exercise.exerciseId] = exercise
    return {"message": "Exercise created", "exercise": exercise}

@app.get("/exercises/{exerciseId}")
def read_exercise(exerciseId: int):
    exercise = exercises.get(exerciseId)
    if exercise:
        return {"exerciseId": exerciseId, "exercise": exercise}
    return {"message": "Exercise not found"}

@app.put("/exercises/{exerciseId}")
def update_exercise(exerciseId: int, updated_exercise: Exercise):
    if exerciseId in exercises:
        exercises[exerciseId] = updated_exercise
        return {"message": "Exercise updated", "exercise": updated_exercise}
    return {"message": "Exercise not found"}

@app.delete("/exercises/{exerciseId}")
def delete_exercise(exerciseId: int):
    if exerciseId in exercises:
        del exercises[exerciseId]
        return {"message": "Exercise deleted"}
    return {"message": "Exercise not found"}
```
