from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='analysis'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('profile/', views.profile_detail, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]