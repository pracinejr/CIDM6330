from django.contrib import admin
from django.urls import path
from .api import api
from soundBody import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),  # Include the API URLs
    # Endpoint to get a custom workout plan for a musician by their ID
    path(
        "api/workouts/custom/<int:musicianId>/",
        views.CustomWorkoutPlanView.as_view(),
        name="custom-workout",
    ),
    # Endpoint to log a completed workout
    path(
        "api/workouts/log/",
        views.WorkoutCompleteEntryView.as_view(),
        name="workout-log",
    ),
]
