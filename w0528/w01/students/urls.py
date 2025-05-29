from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'), # views.py > call list func
    path('write/', views.write, name='write'), # views.py > call write func
    path('update/<str:name>/', views.update, name='update'), # views.py > call update func
    path('delete/<str:name>/', views.delete, name='delete'), # views.py > call delete func
    path('view/', views.view, name='view'), # views.py > call view func
]
