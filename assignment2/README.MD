1. 
    1. ![Alt text](assignment2/images/CIDM_assignment_2.png/)
    > Table musician {
        musicianId int [primary key]
        name varchar
        email varchar
        instrument varchar
        fitnessLevel varchar
      }

      Table trainer {
        trainerId int [primary key]
        name varchar
        email varchar
        expertise varchar
        certification varchar
      }

      Table exercise {
        exerciseId int [primary key]
        name varchar
        instructions text
        muscleGroup varchar
        difficultyLevel varchar
      }

      Table baseWorkoutPlan {
        baseWorkoutPlanId int [primary key]
        name varchar
        duration int
      }

      Table customWorkoutPlan {
        customWorkoutPlanId int [primary key]
        trainerId int [ref: > trainer.trainerId] // A trainer creates custom plans for musicians
        musicianId int [ref: > musician.musicianId] // Assigned to a specific musician
        name varchar
        duration int
      }

      Table baseWorkoutPlanExercise {
        baseWorkoutPlanExerciseId int [primary key]
        baseWorkoutPlanId int [ref: > baseWorkoutPlan.baseWorkoutPlanId]
        exerciseId int [ref: > exercise.exerciseId]
        sets int
        repetitions int
        duration int // Duration per exercise in the workout plan
      }

      Table customWorkoutPlanExercise {
        customWorkoutPlanExerciseId int [primary key]
        customWorkoutPlanId int [ref: > customWorkoutPlan.customWorkoutPlanId]
        exerciseId int [ref: > exercise.exerciseId]
        sets int
        repetitions int
        duration int
      }

      Table workoutCompleteEntry {
        workoutCompleteEntryId int [primary key]
        musicianId int [ref: > musician.musicianId] // The musician who completed the workout
        baseWorkoutPlanId int [ref: > baseWorkoutPlan.baseWorkoutPlanId, null] // Can be a standard plan
        customWorkoutPlanId int [ref: > customWorkoutPlan.customWorkoutPlanId, null] // Or a custom plan
        dateCompleted date
        totalDuration int
        caloriesBurned int
      }

      Table musicianWorkoutStatistics {
        musicianWorkoutStatisticsId int [primary key]
        musicianId int [ref: > musician.musicianId] // Each musician has stats
        totalWorkoutsCompleted int
        totalExercisesCompleted int
        totalTimeSpent int
        averageIntensity varchar
      }
      >
    2. 
    3. 
2. 
3. 