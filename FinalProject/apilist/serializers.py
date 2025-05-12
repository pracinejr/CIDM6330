from rest_framework import serializers
from soundBody.models import CustomWorkoutPlan, WorkoutCompleteEntry


class CustomWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomWorkoutPlan
        fields = [
            "customWorkoutPlanId",
            "name",
            "duration",
            "trainer_id",
            "musician_id",
        ]


class WorkoutCompleteEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutCompleteEntry
        fields = [
            "workoutCompleteEntryId",
            "musicianId",
            "baseWorkoutPlanId",
            "customWorkoutPlanId",
            "dateCompleted",
            "totalDuration",
            "caloriesBurned",
        ]

    def validate_totalDuration(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Total duration must be greater than zero."
            )
        return value

    def validate_caloriesBurned(self, value):
        if value < 0:
            raise serializers.ValidationError("Calories burned cannot be negative.")
        return value
