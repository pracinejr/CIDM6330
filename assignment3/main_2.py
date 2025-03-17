from repository_memory import Exercises, MyMemoryRepo

exercise = Exercises(
    exerciseId=9,
    name="Overhead Press",
    instructions="Stand with feet shoulder-width apart, grip the barbell just outside shoulder width, brace your core, press the bar overhead by extending your arms fully while keeping it in line with your midfoot, lock out at the top, then lower the bar back to shoulder level with control.",
    muscleGroup="shoulders",
    difficultyLevel="Med",
)


def do_memory():

    print("WORKING WITH A MEMORY REPOSITORY")
    repo = MyMemoryRepo("exerciseId")

    # create
    print("Create an exercise in the repository")
    print(f"HEY {type(exercise)}")
    repo.do_create(exercise)
    # print(type(exercise))

    # read
    print("Read the exercise from the repository")
    print(repo.do_read_exercise(9))

    # update
    repo.do_update(9, "muscleGroup", "Shoulders/Chest")

    # read
    print(repo.do_read_exercise(9))

    # delete
    repo.do_delete(9)

    # read
    try:
        print(repo.do_read_exercise(9))
    except KeyError:
        print("Exercise not found")


if __name__ == "__main__":
    do_memory()
