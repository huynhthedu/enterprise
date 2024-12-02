from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the base URL
    path('<int:framework_id>/', views.detail, name='detail'),
]