
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', 'home.urls'),
    path('board/', 'board.urls'),
    path('comment/', include('comment.urls')),
]
