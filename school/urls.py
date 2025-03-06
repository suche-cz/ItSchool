# school/urls.py

from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
]
