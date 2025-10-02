from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'), 
    path('view_food/', views.view_food, name='view_food'),
    path('add_food/', views.add_food, name='add_food'),
    path('remove_food/<int:food_id>/', views.remove_food, name='remove_food'),
    path('calculate_total/', views.calculate_total, name='calculate_total'),
    path('reset_calories/', views.reset_calories, name='reset_calories'),   
]