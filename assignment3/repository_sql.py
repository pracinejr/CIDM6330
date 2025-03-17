from abc import ABC, abstractmethod
from sqlmodel import SQLModel, create_engine, Session, Field, select


# creates a SQLModel
class Exercises(SQLModel, table=True):

    exerciseId: int = Field(default=None, primary_key=True)
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


class MySQLModelRepo(BaseExercisesRepo):

    def __init__(self, db_string="sqlite:///exercise.db"):
        # ability to work use the database
        self.engine = create_engine(db_string)
        # ability to create all tables and structures
        SQLModel.metadata.create_all(self.engine)
        # ability to perform operations on the database
        self.session = Session(self.engine)

    def do_create(self, exercise):
        self.session.add(exercise)
        self.session.commit()

    def do_read_all(self):
        statement = select(Exercises)
        result = self.session.exec(statement)
        return result.all()

    def do_read_exercise(self, exerciseId):
        statement = select(Exercises).where(Exercises.exerciseId == exerciseId)
        result = self.session.exec(statement)
        return result.one()

    def do_read_exercise_name(self, name: str):
        statement = select(Exercises).where(Exercises.name == name)
        result = self.session.exec(statement)
        return result.one()

    def do_update(self, exerciseId, field, value):
        exercise = self.do_read_exercise(exerciseId)

        if field == "name":
            exercise.name = value

        if field == "instructions":
            exercise.instructions = value

        if field == "muscleGroup":
            exercise.muscleGroup = value

        if field == "difficultyLevel":
            exercise.difficultyLevel = value

        self.session.add(exercise)
        self.session.commit()
        self.session.refresh(exercise)

    def do_delete(self, exerciseId):
        exercise = self.do_read_exercise(exerciseId)
        self.session.delete(exercise)
        self.session.commit()
