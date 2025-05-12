from django.contrib import admin
from django.urls import path, include
from .api import api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "apilist/", include("apilist.urls", namespace="apilist")
    ),  # Include the URLs from the apilist app
    path("api/", api.urls),  # Include the API URLs from the apilist app
]
