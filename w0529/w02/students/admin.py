from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ["no", "name", "sdate"]

admin.site.register(Student, StudentAdmin)

