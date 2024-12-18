from django.urls import path
from . import views

urlpatterns = [
    # path('', views.calculate_growth_and_rankings, name='rankings'),
    path('', views.result, name='rankings'),
    path('indicator_map/', views.indicator_map, name='indicator_map'),
    path('chart/', views.growth_chart, name='growth_chart'),
    path('indicator_map/', views.shown_chart, name='shown_chart'),    
    path('scores/', views.score_and_rankings, name='score_and_rankings'),    
    path('result/', views.result, name='result'),    
    path('all_states/', views.all_states, name='all_states'),    
    path('doanhnghiep/', views.doanhnghiep, name='doanhnghiep'),    
]

