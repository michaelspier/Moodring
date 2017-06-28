from django.contrib import admin

# Register your models here.
from .models import Day, Mood, Event, Event_Type

admin.site.register(Mood)
admin.site.register(Event)
admin.site.register(Event_Type)
admin.site.register(Day)
