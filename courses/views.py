<<<<<<< HEAD
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> origin/WCNgApps
from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    context = {'courses' : courses}

    return render(request, 'courses/courses.html', context)


def course(request, course_id):
    course = get_object_or_404(Course,pk=course_id)
    course.total_sit = course.total_sit - course.onenquiry_sit

    context = {'course' : course}
    return render(request, 'courses/course.html', context)