from . import views
from django.urls import path

app_name = 'comment'

urlpatterns = [
    path('list/', views.list, name='list'),
]
