from django.shortcuts import render
import requests
import json

mdlist = []

def list(request):
    serviceKey = '7c21e998e08b6f5e4ce3af29b5f54763'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={serviceKey}&targetDt=20250617'
    response = requests.get(url)        
    jsonData = json.loads(response.text)  
    global mdlist
    mdlist = jsonData['boxOfficeResult']['dailyBoxOfficeList']
    context = {'list':mdlist}
    return render(request, 'pboard3/list.html', context)

def view(request, movieCd):
    global mdlist
    context = {}
    for md in mdlist:
        if md['movieCd'] == str(movieCd):
            context['mdData'] = md
    return render(request, 'pboard3/view.html', context)
 