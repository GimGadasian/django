from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('write/', views.write, name='write'), # call write func in views.py
    path('result/', views.result, name='result'), # call result func in views.py
    
]
