from . import views
from django.urls import path

app_name = 'member'
urlpatterns = [
    
    path('login/', views.login, name='login'),
    path('join01/', views.join01, name='join01'), # 등록
    path('join02/', views.join02, name='join02'), # 정보입력
    path('join03/', views.join03, name='join03'), # 완료
]
