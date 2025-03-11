from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic
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

# /courses/10/

def course_detail(request, pk):
    course = get_object_or_404(models.Course, id=pk)
    return render(request, 'school/course_detail.html', {'course': course})


class CourseDetail(generic.DetailView):
    model = models.Course


class CourseList(generic.ListView):
    # school/course_list.html
    # model = models.Course
    # custom queryset + select related pro optimalizaci napojených záznamů
    queryset  = models.Course.objects.select_related('lector')
    template_name = 'school/courses.html'
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator'] # stará se o stránkování 
        page_obj = context['page_obj'] # objekt reprezentující aktuální stránku
        context['paginator_range'] = paginator.get_elided_page_range(
            page_obj.number,
            on_each_side=1,
            on_ends=1,
        )
        return context

