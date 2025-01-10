# your_app/urls.py (app-level)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.degree, name='degree'),  # Make sure this matches the URL you want
    path('tuition', views.tuition, name='tuition'),  # Make sure this matches the URL you want
    path('error', views.check_error, name='error'),  # Make sure this matches the URL you want
]
