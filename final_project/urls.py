from django.urls import path
from . import views

urlpatterns = [
    path('', views.library, name=''),  # Make sure this matches the URL you want
]
