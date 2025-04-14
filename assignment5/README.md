# Assignment 5

## Screenshots/Images

Below are the screenshots/images included in the `/assignment5Images` folder:

![Alt text](/assignment5/assignment5Images/broker.png)
![Alt text](/assignment5/assignment5Images/cityWeatherPrediction.png)
![Alt text](/assignment5/assignment5Images/loader.png)
![Alt text](/assignment5/assignment5Images/scheduler.png)
![Alt text](/assignment5/assignment5Images/snapShotOfJupiterComputations.png)
![Alt text](/assignment5/assignment5Images/travelRecomendation.png)
![Alt text](/assignment5/assignment5Images/testsPassingInSoundBodyApp.png)

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
