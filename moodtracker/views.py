from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def calendar_view(request, year, month, day, view_period):
    start_date = datetime.strptime('%s/%s/%s' % (year, month, day), '%Y/%m/%d')
    end_date = start_date + timedelta(days=int(view_period))
    output = 'I should be showing events and moods from %s to %s' % (start_date.strftime("%m/%d/%Y"), end_date.strftime("%m/%d/%Y"))
    return HttpResponse(output)

def mood_view(request, mood_id):
    return HttpResponse("Hello, World.")

def event_view(request, event_id):
    return HttpResponse("Hello, World.")

def update_mood(request, mood_id):
    return HttpResponse("Hello, World.")

def update_event(request, event_id):
    return HttpResponse("Hello, World.")

def new_mood(request, start_date, end_date):
    return HttpResponse("Hello, World.")

def new_event(request, start_date, end_date):
    return HttpResponse("Hello, World.")
