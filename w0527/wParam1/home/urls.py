from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'), # call index func in views.py
]
