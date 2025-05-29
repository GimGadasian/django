from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # urls.py in home app
    path('students/', include('students.urls'))
]
