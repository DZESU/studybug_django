from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
rooms = [

    {'id':1, 'name':"Learn Pyhton"},
    {'id':2, 'name':"Learn Pyhton"},
    {'id':3, 'name':"Learn Pyhton"},
]


def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')