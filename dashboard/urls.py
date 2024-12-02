# your_app/urls.py (app-level)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Make sure this matches the URL you want
]
