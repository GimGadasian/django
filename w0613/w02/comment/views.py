from django.shortcuts import render
from django.http import JsonResponse

def list(request):
    context = {'result':'success'}
    return JsonResponse(context)
