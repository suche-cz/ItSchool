from django.shortcuts import render, HttpResponse
from school import models

# views.py

def index(request):
    return render(request, 'school/index.html')

def students(request):
    return render(request, 'school/students.html')

def courses(request):
    courses = models.Course.objects.all()
    return render(
        request,
        'school/courses.html',
        {'courses': courses}
    )
