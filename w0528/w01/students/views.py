from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from students.models import Student

# students info list
def list(request):
    ## get from DB: objects.all(), objects.get(), objects.filter(), objects.order_by()
    #qs = Student.objects.filter(name__contains = "Kim")
    #qs = Student.objects.filter(age__gte=22)
    #qs = Student.objects.order_by('major')
    qs = Student.objects.all()
    context = {'list' : qs}
    return render(request, 'students/list.html', context) # render list.html' in templates > students

# students registration
def write(request):
    if request.method == 'POST': # post: only form
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        #print("input data:", name, major, grade, age, gender)
        ## store in Student table object: .save(), .create()
        Student(name=name, major=major, grade=grade, age=age, gender=gender).save()
        return redirect('/students/list/')
    else:
        # print(request)
        # print(request.GET)
        # print(request.method)
        return render(request, 'students/write.html')

def update(request,name):
    if request.method == "GET": 
        qs = Student.objects.get(name=name)
        context = {"stu": qs}
        return render(request, 'students/update.html', context)
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        #print("input data:", name, major, grade, age, gender)
        ## store in Student table object: .save(), .create()
        qs = Student.objects.get(name=name)
        qs.name = name
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.save()
        
        return redirect('/students/list/')
def delete(request, name):
    qs = Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list')
    
def view(request):
    name = request.GET.get('name')
    print(name)
    qs = Student.objects.get(name=name)
    context = {'stu' : qs}
    return render(request, 'students/view.html', context)