# school/urls.py

from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    # path('courses/', views.courses, name='courses'),
    path('courses/', views.CourseList.as_view(), name='courses'),
    # path('courses/<int:pk>/', views.course_detail, name='course_detail'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
]
