from django.shortcuts import render, redirect
from students.models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'students/list.html', context)

def register(request):
    return render(request, 'students/register.html')

def register2(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    print("data info:", name, major, grade, age, gender)
    
    qs = Student(name= name, major=major, grade=grade, age=age, gender=gender)
    qs.save()

    return redirect('students:list') # app_name
    #return render(request, 'students/register.html')