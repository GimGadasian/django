from . import views
from django.urls import path

app_name = 'board'
urlpatterns = [
    
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('view/<int:bno>/', views.view, name='view'),
    path('update/<int:bno>/', views.update, name='update'),
    
]
