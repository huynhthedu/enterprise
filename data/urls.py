from django.urls import path
from . import views

urlpatterns = [
    path('', views.data, name=''),  # Make sure this matches the URL you want
]
