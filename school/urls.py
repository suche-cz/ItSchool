# school/urls.py

from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [
    path('', views.index),
    path('students/', views.students),
    path('courses/', views.courses),
]

