from __future__ import annotations

from django.urls import path

from api.views import health

urlpatterns = [
    path("health/", health),
]

