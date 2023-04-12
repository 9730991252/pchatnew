
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('group/<str:group_name>/', views.group_name, name='group_name'),
    path('join_group/', views.join_group, name='join_group'),
    path('education_ssc/', views.education_ssc, name='education_ssc'),
    path('hsc_college/', views.hsc_college, name='hsc_college'),
    path('my_group/', views.my_group, name='my_group'),

    path('select_year_group/', views.select_year_group, name='select_year_group'),
    path('select_year_hsc/', views.select_year_hsc, name='select_year_hsc'),
    path('participants_login/', views.participants_login,name='participants_login'),
    path('participants_add/', views.participants_add, name='participants_add'),
    path('add_new_school/', views.add_new_school, name='add_new_school'),
    path('add_new_college/', views.add_new_college, name='add_new_college'),



]
