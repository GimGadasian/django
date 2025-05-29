from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'), # url: list/ > call def list(request):
    path('register/', views.register, name='register'), # 학생 등록
    path('register2/', views.register2, name='register2') # 학생 저장
]
