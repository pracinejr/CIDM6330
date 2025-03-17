from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Dict


@dataclass
class Exercises:
    exerciseId: int
    name: str
    instructions: str
    muscleGroup: str
    difficultyLevel: str


class BaseExercisesRepo(ABC):
    @abstractmethod
    def do_create(self, exercise):
        pass

    @abstractmethod
    def do_read_all(self):
        pass

    @abstractmethod
    def do_read_exercise(self, exerciseId):
        pass

    @abstractmethod
    def do_read_exercise_name(self, name: str):
        pass

    @abstractmethod
    def do_update(self, exerciseId, field, value):
        pass

    @abstractmethod
    def do_delete(self, exerciseId):
        pass


class MyMemoryRepo(BaseExercisesRepo):

    def __init__(self, id_field: str = "exerciseId"):
        self.repo: Dict[int, Exercises] = {}  # Store exercises in a dictionary
        self.id_field = id_field  # Store ID field name (if needed)

    def do_create(self, exercise: Exercises):
        if not isinstance(exercise, Exercises):
            raise TypeError(f"Expected Exercises object, got {type(exercise)} instead.")

        exercise_id = getattr(exercise, self.id_field)

        if exercise_id in self.repo:
            raise ValueError(f"Exercise with ID {exercise_id} already exists.")

        self.repo[exercise_id] = exercise

    def do_read_all(self) -> list:
        return list(self.repo.values())

    def do_read_exercise(self, exerciseId: int) -> Exercises:
        return self.repo.get(exerciseId, None)

    def do_read_exercise_name(self, exercise_name: str) -> Exercises:
        """Retrieves an exercise by name"""
        for exercise in self.repo.values():
            if exercise.name.lower() == exercise_name.lower():  # Case-insensitive match
                return exercise
        return None  # Return None if no match is found

    def do_update(self, exerciseId: int, field, value):
        if exerciseId not in self.repo:
            raise KeyError(f"Exercise with ID {exerciseId} not found.")
        exercise = self.repo[exerciseId]
        setattr(exercise, field, value)

    def do_delete(self, exerciseId: int):
        if exerciseId in self.repo:
            del self.repo[exerciseId]
        else:
            raise KeyError(f"Exercise with ID {exerciseId} does not exist.")
