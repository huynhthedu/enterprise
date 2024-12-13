from django.urls import path
from . import views
from .views import upload_image, image_list

urlpatterns = [
    path('', views.index, name='index'),  # Add this line for the base URL
    path('<int:framework_id>/', views.detail, name='detail'),
        path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
]