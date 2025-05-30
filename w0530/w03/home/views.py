from django.shortcuts import render

def index(request):
    cook_info = request.COOKIES
    context = {'cook_info' : cook_info}
    user_id = ''
    if request.method == 'POST':
        user_id = request.POST.get('id')
    response = render(request, 'index.html', context)
    if user_id:
        # 쿠키에 id 저장 (1일간 유지)
        response.set_cookie('id', user_id, max_age=60*60*24)
    return response
    
