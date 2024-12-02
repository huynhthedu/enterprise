from django.urls import path
from .views import survey_view

urlpatterns = [
    path('', survey_view, name='survey'),
]
