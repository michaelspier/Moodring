from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def calendar_view(request, year, month, day, view_period):
    return HttpResponse("Hello, World.")

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
