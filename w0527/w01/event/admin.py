from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ["no", "title", "startdate", "enddate", "rdate"]
    
admin.site.register(Event, EventAdmin)