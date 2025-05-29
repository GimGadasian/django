from django.shortcuts import render, redirect
from students.models import Student
def write(request):
    return render(request, 'students/write.html')

def writeOK(request):
    name = request.POST["name"]
    major = request.POST["major"]
    grade = request.POST["grade"]
    age = request.POST["age"]
    gender = request.POST["gender"]
    hobby = request.POST["hobby"] # list
    hobby = ','.join(hobby)
    
    Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby, memo='등록합니다').save()
    return redirect('/students/list/')

def update(request, no):
    qs = Student.objects.get(no=no)
    context = {"student" : qs}
    return render(request, 'students/update.html', context)

def updateOK(request):
    no = request.POST.get("no")
    qs = Student.objects.get(no=no)
    qs.name = request.POST.get('name')
    qs.major = request.POST.get('major')
    qs.grade = request.POST.get('grade')
    qs.age = request.POST.get('age')
    qs.gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    qs.hobby = hobby
    qs.save()
    return redirect('/students/list/')


def view(request, no):
    qs = Student.objects.get(no=no)
    context = {"student" : qs}
    return render(request, 'students/view.html', context)

def list(request):
    qs = Student.objects.all()
    context = {'list' : qs}
    return render(request, 'students/list.html', context)

def delete(request,no):
    Student.objects.get(no=no).delete()
    # return redirect('/students/list/') # url -> name
    return redirect('students:list')   # app_name, path name

    