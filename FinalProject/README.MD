# Assignment 1

1. **Front matter**

- Front page
  - Title: SoundBody
  - Version: 1.0
  - Date: 2/9/2025
  - Author: Peter Racine Jr.
- Introduction

  - SoundBody is a mobile fitness application tailored for musicians, focusing on endurance, flexibility, posture and stength. The app generates personalized workout plans based on instrument type, practice hours, and personal pain-points and physical needs.

- ?Table of contents?

2. **Requirements statements**

   1. User Stories

      1. As a musician, I want to receive personalized workouts based on my playing style so I can improve my endurance and prevent injuries.
      2. As a drummer, I want targeted warm-ups for my wrists and shoulders to avoid strain.
      3. As a guitarist, I want finger flexibility exercises to improve dexterity.
      4. As a bassist, I want to increase my lower back strength so I can sustain activity on stage for multiple hours, multiple nights a week.
      5. As a user, I want to track my progress over time so I can stay motivated.
      6. As a fitness trainer, I want to contribute exercises to the app’s database.

   2. Use Cases

      1. User creates a fitness profile.
      2. App generates a workout plan.
      3. User logs and tracks progress.
      4. App syncs with wearables for real-time feedback.
      5. Trainer submits new exercises.

   3. Features

      1. Musician-specific workouts
      2. Customizable plans
      3. Progress tracking
      4. Wearable integration
      5. AI-powered exercise recommendations

   4. Gherkin Validation
      > Scenario 1: User receives a personalized workout plan
      >
      > - Given the user inputs their instrument type, daily practice hours, >and physical needs
      > - When they submit their profile
      > - Then the app generates a custom workout plan

   > Scenario 2: User logs a workout
   >
   > - Given the user completes an exercise
   > - When they log the activity
   > - Then the app updates their progress and provides feedback

3. **Specifications**

   1. Concept

   - A mobile application that acts as a personal trainer for musicians, helping them stay in peak performance shape through targeted fitness routines.

   2. UX Notes
      1. Simple onboarding
      2. Clear, guided workouts
      3. Gamification elements for motivation
      4. Wearable compatibility
   3. Interfaces (Controls)
      1. Profile setup form
      2. Workout selection
      3. Timer & progress tracker
      4. Sync with smartwatches
   4. Behaviors
      1. ![Alt text](/FinalProject/images/UML_SoundBody_V1.png)

# Assigment 2

**ERD and Python API**

1.

- ![Alt text](/FinalProject/images/CIDM_assignment_2.png)
- [Download the PDF](/FinalProject/images/CIDM_assignment_2.pdf)

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

# Assignment 4

## Screenshots/Images

Below are the screenshots/images included in the `/assignment4Images` folder:

![Alt text](/FinalProject/images/celery.png)
![Alt text](/FinalProject/images/celeryRunning.png)
![Alt text](/FinalProject/images/additionAndMultiply.png)
![Alt text](/FinalProject/images/DjangoAPIRunning.png)
![Alt text](/FinalProject/images/getAllMusicians.png)
![Alt text](/FinalProject/images/getMusicianById.png)
![Alt text](/FinalProject/images/DjangoAPIRunning.png)
![Alt text](/FinalProject/images/ninjaAPI.png)

# Assignment 5

## Screenshots/Images

Below are the screenshots/images included in the `/assignment5Images` folder:

![Alt text](/FinalProject/images/broker.png)
![Alt text](/FinalProject/images/cityWeatherPrediction.png)
![Alt text](/FinalProject/images/loader.png)
![Alt text](/FinalProject/images/scheduler.png)
![Alt text](/FinalProject/images/snapShotOfJupiterComputations.png)
![Alt text](/FinalProject/images/travelRecomendation.png)
![Alt text](/FinalProject/images/testsPassingInSoundBodyApp.png)

```
NOTES:
1. I completed the tutorial in the 'assignment5' directory.
2. I used what I learned to update 'assignment4' code/app so and simply added an 'assign5_custom_operations' directory to 'assignment4' to keep all the work I hade done in that path.
3. Wow. What a ride.

```

1. **Ubiquitous Language Glossary:**

   1. Musician

      - Definition: An individual who engages with the platform to enhance their musical skills through structured training programs.​
      - Role: Primary user who undertakes workout plans and tracks progress.​

   2. Trainer

      - Definition: A professional who creates and assigns workout plans to musicians, monitoring their progress and providing feedback.​
      - Role: Content creator and mentor within the platform.​

   3. Base Workout Plan

      - Definition: A standardized set of exercises designed to address general training objectives for musicians.​
      - Purpose: Serves as a foundational program that can be utilized as-is or customized further.​

   4. Custom Workout Plan

      - Definition: A personalized workout regimen tailored to a musician's specific needs, and can be derived from a base workout plan.​
      - Purpose: Provides targeted training to address individual goals or areas of improvement.​

   5. Exercise

      - Definition: A specific activity or task within a workout plan aimed at improving a particular skill or technique.​
      - Attributes: Includes details such as duration, intensity, and instructions.​

   6. Base Workout Plan Exercise

      - Definition: An exercise that is part of a base workout plan, representing a standard activity applicable to a broad audience.​
      - Purpose: Forms the building blocks of general training programs.​

   7. Custom Workout Plan Exercise

      - Definition: An exercise within a custom workout plan, potentially modified from its base version to suit individual requirements.​
      - Purpose: Ensures exercises are aligned with the musician's personalized training objectives.​

   8. Musician Workout Statistics

      - Definition: Data collected from a musician's workout sessions, including metrics like completion rates, performance scores, and progress over time.​
      - Purpose: Provides insights into a musician's development and areas needing attention.​

   9. Workout Completion Entry

      - Definition: A record indicating the completion of a workout session by a musician, capturing details such as date, time, and performance notes.​
      - Purpose: Tracks adherence to workout plans and facilitates progress monitoring.​

2. **Gherkin Validation**

> > _Scenario 1: User Receives a Personalized Workout Plan_
>
> - _Given_ the user inputs their instrument type, daily practice hours, and physical needs
> - _When_ they submit their profile
> - _Then_ the app generates a custom workout plan

> _Scenario 2: User Logs a Workout_
>
> - _Given_ the user completes an exercise
> - _When_ they log the activity
> - _Then_ the app updates their progress and provides feedback

> _Scenario 3: Trainer Assigns a Base Workout Plan_
>
> - _Given_ a trainer has created a new base workout plan
> - _When_ they assign this plan to a specific musician
> - _Then_ the musician receives a notification and the plan appears in their dashboard

> _Scenario 4: Musician Customizes Their Workout Plan_
>
> - _Given_ a musician has an assigned base workout plan
> - _When_ they modify exercises to better fit their personal goals
> - _Then_ a custom workout plan is created, reflecting their adjustments

> _Scenario 5: Musician Tracks Exercise Completion_
>
> - _Given_ a musician is following a custom workout plan
> - _When_ they mark an exercise as completed
> - _Then_ the app updates their workout completion entry and adjusts their progress statistics

> _Scenario 6: Trainer Reviews Musician Progress_
>
> - _Given_ a musician has been logging their workouts
> - _When_ a trainer accesses the musician's profile
> - _Then_ they can view detailed workout statistics and completion history

> _Scenario 7: Musician Receives Feedback on Performance_
>
> - _Given_ a musician has completed a series of exercises
> - _When_ the system analyzes their performance data
> - _Then_ the musician receives tailored feedback to improve their technique

> _Scenario 8: Trainer Updates Base Workout Plan_
>
> - _Given_ a base workout plan is outdated
> - _When_ a trainer edits the plan to include new exercises
> - _Then_ all musicians assigned to this plan are notified of the updates

> _Scenario 9: Musician Sets Practice Reminders_
>
> - _Given_ a musician wants to maintain a consistent practice schedule
> - _When_ they set daily reminders within the app
> - _Then_ the app sends notifications at the specified times

> _Scenario 10: Musician Shares Progress with Trainer_
>
> - _Given_ a musician has achieved a milestone in their training
> - _When_ they choose to share their progress
> - _Then_ the trainer receives a summary of the musician's achievements
