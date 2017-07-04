from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    #The Root, index view
    url(r'^$', views.index, name='index'),
    #The Mood View, ex: /moodtracker/mood/5/
    url(r'^mood/(?P<mood_id>[0-9]+)/$', views.mood_view, name='mood_detail'),
    #The event view, ex: /moodtracker/event/5/
    url(r'^event/(?P<event_id>[0-9]+)/$', views.event_view, name='event_detail'),
    #the url below drives the calendar view, which is expecting URLS in
    #the following format: /moodtracker/calendar/2017/03/01/30/, where the
    #numbers after calendar represent the year, month, day, and period of
    #the view
    url(r'^calendar/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d+)/(?P<view_period>[0-9]+)/$', views.calendar_view, name='calendar'),
]
