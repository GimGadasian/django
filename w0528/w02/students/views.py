from django.shortcuts import render, redirect
from students.models import Student

def list(request): # rendering simple students information list
    qs = Student.objects.all()
    context = {'list' : qs}
    return render(request, 'students/list.html', context)

def add(request): # add student
    if request.method == "POST": # form
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        Student(name=name, major=major, grade=grade, age=age, gender=gender).save()
        return redirect('../list')
    return render(request, "students/add.html") # else: not form
    
def details(request): # show detailed information of the selected student
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    context = {"st" : qs}
    return render(request, 'students/details.html', context)