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
