from django.urls import path
from .views import dashboard

app_name = "trots"

urlpatterns = [
    path("", dashboard, name="dashboard"),
]
