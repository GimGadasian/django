from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path('', views.index, name='index'), # views.py > call index func
]
