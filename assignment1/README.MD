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
      >- Given the user inputs their instrument type, daily practice hours, >and physical needs  
      >- When they submit their profile  
      >- Then the app generates a custom workout plan  

    > Scenario 2: User logs a workout  
      >- Given the user completes an exercise  
      >- When they log the activity  
      >- Then the app updates their progress and provides feedback  


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
        1. ![Alt text](/assignment1/images/UML_SoundBody_V1.png)

