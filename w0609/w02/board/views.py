from django.shortcuts import render, redirect
from django.http import JsonResponse

def list(request):
    return render(request, 'board/list.html')

def view(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        context = {'id':id, 'name':name}
        return render(request, 'board/view.html', context)
    else:
        return 0
    
def view2(request):
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    context = {'id':id, 'name':name, 'result':'successed', 'pw':'1111'}
    return JsonResponse(context)