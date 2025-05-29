from django.shortcuts import render
from students.models import Student

# students information in db -> simple list
def list(request):
    qs = Student.objects.all()
    context = {"list" : qs}
    return render(request, 'students/list.html', context)
