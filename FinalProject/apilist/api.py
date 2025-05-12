from ninja import NinjaAPI
from ninja import Schema, Field
from datetime import date
from ninja import UploadedFile, File
from soundBody.models import Musician
from soundBody.models import Exercise
from soundBody.models import Trainer
from django.shortcuts import get_object_or_404
from typing import Optional
from pydantic import Field


api = NinjaAPI()


class MusicianIn(Schema):
    musicianId: int
    name: str
    email: str
    instrument: str
    fitnessLevel: str
    joinDate: date = Field(default_factory=date.today)


class MusicianOut(Schema):
    musicianId: int
    name: str
    email: str
    instrument: str
    fitnessLevel: str
    joinDate: date = Field(default_factory=date.today)


class MusicianUpdate(Schema):
    name: Optional[str]
    email: Optional[str]
    instrument: Optional[str]
    fitnessLevel: Optional[str]
    joinDate: Optional[date] = Field(default_factory=date.today)


class ExerciseIn(Schema):
    exerciseId: int
    name: str
    instructions: str
    muscleGroup: str
    difficultyLevel: str
    joinDate: date = Field(default_factory=date.today)


class ExerciseOut(Schema):
    exerciseId: int
    name: str
    instructions: str
    muscleGroup: str
    difficultyLevel: str


class ExerciseUpdate(Schema):
    name: Optional[str]
    instructions: Optional[str]
    muscleGroup: Optional[str]
    difficultyLevel: Optional[str]


class TrainerIn(Schema):
    trainerId: int
    name: str
    email: str
    expertise: str
    certification: str
    joinDate: date = Field(default_factory=date.today)


class TrainerOut(Schema):
    trainerId: int
    name: str
    email: str
    expertise: str
    certification: str
    joinDate: date = Field(default_factory=date.today)


class TrainerUpdate(Schema):
    name: Optional[str]
    email: Optional[str]
    expertise: Optional[str]
    certification: Optional[str]
    joinDate: Optional[date] = Field(default_factory=date.today)


@api.get("/hello")
def hello(request):
    return {"message": "Hello, world!"}


@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}


@api.get("/musicians/")
def list_musicians(request):
    musicians = Musician.objects.all()
    return [MusicianOut.from_orm(musician) for musician in musicians]


@api.post("/musicians/")
def create_musician(request, musician: MusicianIn, cv: UploadedFile = File(...)):
    payload_info = musician.dict()
    payload = Musician(**payload_info)
    musician = Musician.objects.create(payload)
    payload.cv.save(cv.name, cv)
    return MusicianOut.from_orm(musician)


@api.get("/musicians/{musicianId}")
def read_musician(request, musicianId: int):
    musician = get_object_or_404(Musician, musicianId=musicianId)
    return MusicianOut.from_orm(musician)


@api.put("/musicians/{musicianId}")
def update_musician(request, musicianId: int, updated_musician: MusicianUpdate):
    musician = get_object_or_404(Musician, musicianId=musicianId)
    for attr, value in updated_musician.dict().items():
        setattr(musician, attr, value)
    musician.save()
    return MusicianOut.from_orm(musician)


@api.delete("/musicians/{musicianId}")
def delete_musician(request, musicianId: int):
    musician = get_object_or_404(Musician, musicianId=musicianId)
    musician.delete()
    return {"message": "Musician deleted"}


@api.post("/exercises/")
def create_exercise(request, exercise: ExerciseIn, cv: UploadedFile = File(...)):
    payload_info = exercise.dict()
    payload = Exercise(**payload_info)
    exercise = Exercise.objects.create(payload)
    payload.cv.save(cv.name, cv)

    return exercise


@api.get("/exercises/{exerciseId}")
def read_exercise(request, exerciseId: int):
    exercise = get_object_or_404(Exercise, exerciseId=exerciseId)
    return exercise


@api.put("/exercises/{exerciseId}")
def update_exercise(request, exerciseId: int, updated_exercise: ExerciseIn):
    exercise = get_object_or_404(Exercise, exerciseId=exerciseId)
    for attr, value in updated_exercise.dict().items():
        setattr(exercise, attr, value)
    exercise.save()
    return exercise


@api.delete("/exercises/{exerciseId}")
def delete_exercise(request, exerciseId: int):
    exercise = get_object_or_404(Exercise, exerciseId=exerciseId)
    exercise.delete()
    return {"message": "Exercise deleted"}


@api.post("/trainers/")
def create_trainer(request, trainer: TrainerIn, cv: UploadedFile = File(...)):
    payload_info = trainer.dict()
    payload = Trainer(**payload_info)
    trainer = Trainer.objects.create(payload)
    payload.cv.save(cv.name, cv)

    return trainer


@api.get("/trainers/{trainerId}")
def read_trainer(request, trainerId: int):
    trainer = get_object_or_404(Trainer, trainerId=trainerId)
    return trainer


@api.put("/trainers/{trainerId}")
def update_trainer(request, trainerId: int, updated_trainer: TrainerIn):
    trainer = get_object_or_404(Trainer, trainerId=trainerId)
    for attr, value in updated_trainer.dict().items():
        setattr(trainer, attr, value)
    trainer.save()
    return trainer


@api.delete("/trainers/{trainerId}")
def delete_trainer(request, trainerId: int):
    trainer = get_object_or_404(Trainer, trainerId=trainerId)
    trainer.delete()
    return {"message": "Trainer deleted"}


# The above code defines a Django Ninja API with CRUD operations for Musician, Exercise, and Trainer models.
# It includes endpoints for creating, reading, updating, and deleting records in the database.
