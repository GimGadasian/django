from django.shortcuts import render

def write(request):
    return render(request, 'students/write.html')

def result(request):
    # get data from form
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbies = request.POST.getlist('hobbies')
    
    context = {'id': id, 'pw': pw, 'name' : name, 'age': age, 'gender':gender ,'hobbies': hobbies}
    return render(request, 'students/result.html', context)
