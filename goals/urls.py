from django.urls import path
from . import views

urlpatterns = [
    path( '', views.get_grading_parameters, name = 'index' ),
    path( 'todaysdate/', views.current_datetime),
    path( 'addgoal/', views.add_goal)
]   