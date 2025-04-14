from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
import json
from soundBody.models import (
    Musician,
    Trainer,
    Exercise,
    BaseWorkoutPlan,
    CustomWorkoutPlan,
)


class MusicianTrainerWorkflowTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.trainer = Trainer.objects.create(
            name="Jane Trainer",
            email="jane@trainer.com",
            expertise="Posture",
            certification="NASM",
            joinDate=date.today(),
        )
        self.musician = Musician.objects.create(
            name="John Musician",
            email="john@music.com",
            instrument="Drums",
            fitnessLevel="Intermediate",
            joinDate=date.today(),
        )
        self.exercise = Exercise.objects.create(
            name="Wrist Stretch",
            instructions="Stretch wrist for 30s",
            muscleGroup="Forearm",
            difficultyLevel="Easy",
        )
        self.base_plan = BaseWorkoutPlan.objects.create(
            name="Basic Drum Prep", duration=30
        )
        self.custom_plan = CustomWorkoutPlan.objects.create(
            name="John's Drum Plan",
            duration=45,
            trainer=self.trainer,
            musician=self.musician,
        )

    def test_personalized_plan_creation(self):
        """
        Scenario: User receives a personalized workout plan
        Given the user inputs their instrument type, daily practice hours, and physical needs
        When they submit their profile
        Then the app generates a custom workout plan
        """
        response = self.client.get(f"/api/workouts/custom/{self.musician.musicianId}/")
        print("Response JSON:", response.json())
        self.assertEqual(response.status_code, 200)

    def test_logging_workout(self):
        """
        Scenario: User logs a workout
        Given the user completes an exercise
        When they log the activity
        Then the app updates their progress and provides feedback
        """
        log_data = {
            "musicianId": self.musician.musicianId,
            "customWorkoutPlanId": self.custom_plan.customWorkoutPlanId,
            "dateCompleted": str(date.today()),
            "totalDuration": 45,
            "caloriesBurned": 300,
        }

        response = self.client.post(
            reverse("workout-log"),
            data=json.dumps(log_data),
            content_type="application/json",
        )
        print("RESPONSE JSON:", response.json())
        self.assertEqual(response.status_code, 201)
