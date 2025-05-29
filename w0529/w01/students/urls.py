
from . import views
from django.urls import path

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('writeOK/', views.writeOK, name='writeOK'),
    path('update/<int:no>/', views.update, name='update'),
    path('updateOK/', views.updateOK, name='updateOK'),
    path('view/<int:no>/', views.view, name='view'),
    path('delete/<int:no>/', views.delete, name='delete'),
]
