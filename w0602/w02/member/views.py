from django.shortcuts import render
from member.models import Member

def login(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idCheck = request.POST.get('idCheck')
        
        # login check
        try:
            qs = Member.get(id=id, pw=pw)
        except:
            context = {'msg' : 0} # login failed
            return render(request, 'member/login.html', context)
        
        # store cookie in 'response'
        request.session['session_id'] = id
        request.session['session_nick'] = qs.nick # object of Member, undefined in here
        
        context = {'msg' : 1} # login sucessed
        response = render(request, 'member/login.html', context)
        
        if idCheck != None: # store cookie for a day
            response.set_cookie('idCheck', id, max_age=60*60*24)
        else:
            response.delete_cookie('idCheck') # delete cookie
        return response

    else: # request.method == 'GET'
        idCheck = request.COOKIES.get('idCheck', '')
        
        
     
