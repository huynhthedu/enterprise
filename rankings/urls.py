from django.urls import path
from . import views

app_name = 'rankings'

urlpatterns = [    
    path('', views.dashboard_view, name='rankings'),
    path('indicator_map/', views.indicator_map, name='indicator_map'),
    path('chart/', views.growth_chart, name='growth_chart'),
    path('indicator_map/', views.shown_chart, name='shown_chart'),            
    path('select_state/', views.select_state, name='select_state'), 
    path('one_year/<int:pk>/', views.one_year, name='one_year'), 
    path('dashboard/', views.state, name='dashboard'),
    path('get_indicator_data/', views.get_indicator_data, name='get_indicator_data'),
    path('get_year_data/', views.get_year_data, name='get_year_data'),
    path('overall_indicator/', views.overall_indicator, name='overall_indicator'),
    

    # path('state/', views.state, name='state'),        
]

