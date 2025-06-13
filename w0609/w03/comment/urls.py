from . import views
from django.urls import path

app_name = 'comment'
urlpatterns = [
    
    path('cwrite/', views.cwrite, name='cwrite'),
    path('cdelete/', views.cdelete, name='cdelete'),
   
    
]
