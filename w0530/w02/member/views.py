from django.shortcuts import render, redirect
from member.models import Member

def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        try:
            msg = 1
            qs = Member.objects.get(id=id, pw=pw)
            request.session['session_id'] = qs.id
            request.session['session_nickName'] = qs.nickName
            return redirect('/')
        except:
            msg = 0
        context = {'msg' : msg}
        response = render(request, 'member/login.html', context)
       
    else: return render(request, 'member/login.html')

def logout(request):
    msg = -1
    request.session.clear()
    context = {'msg': msg}
    
    return redirect('/',context)        