from django.shortcuts import render

def list(request):
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    phone = request.POST.get('phone')
    
    
    context = {'id' : id, 'pw' : pw, "phone" : phone}
    return render(request, 'students/list.html', context)

def view(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {'name': name, 'age': age}
    return render(request, 'students/view.html', context)

def write(request):
    return render(request, 'students/write.html')

def result(request):
    name = request.POST.get('name')
    kor = request.POST.get('kor')
    eng = request.POST.get('eng')
    math = request.POST.get('math')
    hobbys = request.POST.getlist('hobby')
    
    context = {'name': name, 'kor': kor, 'eng' : eng, 'math': math, 'hobbys': hobbys}
    return render(request, 'students/result.html', context)

def send(request, name, age):
    context = {'name': name, 'age' : age}
    return render(request, 'students/send.html', context)    
    