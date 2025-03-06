from django.shortcuts import render, HttpResponse

# views.py

def index(request):
    return render(request, 'school/index.html')

def students(request):
    return render(request, 'school/students.html')

def courses(request):
    return render(request, 'school/courses.html')
