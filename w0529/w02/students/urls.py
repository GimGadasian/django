
from . import views
from django.urls import path, include

app_name = 'students'
urlpatterns = [
    
    path('list/', views.list, name="list"),
]
