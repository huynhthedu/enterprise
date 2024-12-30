from django.urls import path
from . import views

urlpatterns = [    
    path('', views.state, name='rankings'),
    path('indicator_map/', views.indicator_map, name='indicator_map'),
    path('chart/', views.growth_chart, name='growth_chart'),
    path('indicator_map/', views.shown_chart, name='shown_chart'),            
    path('select_state/', views.select_state, name='select_state'), 
    path('one_year/', views.one_year, name='one_year'), 
    # path('state/', views.state, name='state'),        
]

