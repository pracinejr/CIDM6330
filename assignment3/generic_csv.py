from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict, field, InitVar
import csv


@dataclass
class Exercise:
    exerciseId: int
    name: str
    instructions: str
    muscleGroup: str
    difficultyLevel: str


class ExerciseRepository(ABC):
    @abstractmethod
    def do_create(self, exercise: Exercise):
        pass

    @abstractmethod
    def read_all(self):
        pass

    @abstractmethod
    def do_read(self, exerciseId):
        pass

    @abstractmethod
    def do_update(self, exerciseId, exercise: Exercise):
        pass

    @abstractmethod
    def do_delete(self, exerciseId):
        pass


class MyCSVRepo(ExerciseRepository):

    def __init__(self, filename: str, id_field: str, fieldnames: list):

        self.repo = list[Exercise]  # this is a typehint for a list of Exercise objects
        self.filename = filename
        self.fieldnames = fieldnames

        with open(filename, mode="r", newline="") as file:
            csv_reader = csv.DictReader(file)
            self.repo = [Exercise(**row) for row in csv_reader]

    def do_create(self, exercise: Exercise):
        self.repo.append(exercise)
        self.do_save_file()

    def read_all(self):
        return self.repo

    def do_read(self, exerciseId):
        return self.repo[str(exerciseId)]

    def do_update(self, exerciseId, exercise: Exercise):
        self.repo[str(exerciseId)] = exercise
        self.do_save_file()

    def do_delete(self, exerciseId):
        for exercise in self.repo:
            if int(exercise.exerciseId) == int(exerciseId):
                self.repo.remove(exercise)
                break

        self.do_save_file()

    def do_save_file(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for exercise in self.repo:
                writer.writerow(asdict(exercise))


class MyMemoryRepo(ExerciseRepository):

    def __init__(self, id_field: str):

        self.repo = list[Exercise]

    def do_create(self, exercise: Exercise):
        self.repo.append(exercise)

    def read_all(self):
        return self.repo

    def do_read(self, exerciseId):
        return self.repo[exerciseId]

    def do_update(self, exerciseId, exercise: Exercise):
        self.repo[exerciseId] = exercise

    def do_delete(self, exerciseId):
        for exercise in self.repo:
            if int(exercise.exerciseId) == int(exerciseId):
                self.repo.remove(exercise)
                break


# Defining main function
def main():
    print("generic repository example")
    csv_repo = MyCSVRepo(
        "exercises.csv",
        "exerciseId",
        ["exerciseId", "name", "instructions", "muscleGroup", "difficultyLevel"],
    )
    # csv_repo.do_create(
    #     Exercise(
    #         9,
    #         "Overhead Press",
    #         "Stand with feet shoulder-width apart, grip the barbell just outside shoulder width, brace your core, press the bar overhead by extending your arms fully while keeping it in line with your midfoot, lock out at the top, then lower the bar back to shoulder level with control.",
    #         "shoulders",
    #         "Med",
    #     )
    # )

    # csv_repo.do_create(
    #     Exercise(
    #         10,
    #         "Squat",
    #         "Stand with feet shoulder-width apart, keep your chest up, engage your core, lower your body by bending your knees and pushing your hips back until your thighs are parallel to the floor, keep your knees aligned with your toes, then push through your heels to return to the starting position.",
    #         "Legs",
    #         "High",
    #     )
    # )

    # csv_repo.do_create(
    #     Exercise(
    #         11,
    #         "Deadlift",
    #         "Stand with feet hip-width apart, grip the barbell with hands just outside your knees, keep your back straight and core engaged, hinge at your hips and lower the bar while keeping it close to your body, then drive through your heels, extending your hips and knees to lift the bar to a standing position, squeezing your glutes at the top before lowering it back down with control.",
    #         "Low back",
    #         "High",
    #     )
    # )

    csv_repo.do_create(
        Exercise(
            12,
            "Bench Press",
            "Lie flat on a bench, grip the bar slightly wider than shoulder-width, lower the bar to your chest, keeping elbows at a 45-degree angle, then push the bar back up to arm’s length, fully extending your arms..",
            "Chest",
            "Low",
        )
    )

    # csv_repo.do_delete(12)

    print(csv_repo.read_all())


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
