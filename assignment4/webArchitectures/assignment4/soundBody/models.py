from django.db import models
from datetime import date


# Create your models here.
class Musician(models.Model):
    musicianId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    instrument = models.CharField(max_length=100)
    fitnessLevel = models.CharField(max_length=50)
    joinDate = models.DateField(default=date.today)
    cv = models.FileField(null=True, blank=True)


class Exercise(models.Model):
    exerciseId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    muscleGroup = models.CharField(max_length=50)
    difficultyLevel = models.CharField(max_length=50)
    cv = models.FileField(null=True, blank=True)


class Trainer(models.Model):
    trainerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    expertise = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    joinDate = models.DateField(default=date.today)
    cv = models.FileField(null=True, blank=True)
    # def __str__(self):
    # return self.name


class BaseWorkoutPlan(models.Model):
    baseWorkoutPlanId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    duration = models.IntegerField()  # duration in minutes


class CustomWorkoutPlan(models.Model):
    customWorkoutPlanId = models.AutoField(primary_key=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    duration = models.IntegerField()  # duration in minutes


class BaseWorkoutPlanExercise(models.Model):
    baseWorkoutPlanExerciseId = models.AutoField(primary_key=True)
    baseWorkoutPlan = models.ForeignKey(BaseWorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    duration = models.IntegerField()  # duration per exercise in minutes


class CustomWorkoutPlanExercise(models.Model):
    customWorkoutPlanExerciseId = models.AutoField(primary_key=True)
    customWorkoutPlan = models.ForeignKey(CustomWorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    repetitions = models.IntegerField()
    duration = models.IntegerField()


class WorkoutCompleteEntry(models.Model):
    workoutCompleteEntryId = models.AutoField(primary_key=True)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    baseWorkoutPlan = models.ForeignKey(
        BaseWorkoutPlan, on_delete=models.SET_NULL, null=True, blank=True
    )
    customWorkoutPlan = models.ForeignKey(
        CustomWorkoutPlan, on_delete=models.SET_NULL, null=True, blank=True
    )
    dateCompleted = models.DateField()
    totalDuration = models.IntegerField()
    caloriesBurned = models.IntegerField()


class MusicianWorkoutStatistics(models.Model):
    musicianWorkoutStatisticsId = models.AutoField(primary_key=True)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    totalWorkoutsCompleted = models.IntegerField()
    totalExercisesCompleted = models.IntegerField()
    totalTimeSpent = models.IntegerField()
    averageIntensity = models.CharField(max_length=50)
