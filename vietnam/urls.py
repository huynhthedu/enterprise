# your_app/urls.py (app-level)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.vietnam, name='vietnam'),     
]
