from django.urls import path
from . import views

app_name = "apilist"
# app_name is used to namespace the URLs in this app

urlpatterns = [
    path("signup/", views.UserRegistration.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("user-list/", views.UserListAPIView.as_view(), name="user-list"),
    path(
        "coolest-districts/",
        views.CoolestDistrictsAPIView.as_view(),
        name="coolest-districts",
    ),
    path(
        "recommendation/",
        views.DecisionMakingAPIView.as_view(),
        name="travel-recommendation",
    ),
    path(
        "predict-weather/",
        views.WeatherPredictionAPIView.as_view(),
        name="predict-weather",
    ),
]
