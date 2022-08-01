from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
rooms = [

    {'id': 1, 'name': "Learn Pyhton 1"},
    {'id': 2, 'name': "Learn Pyhton 2"},
    {'id': 3, 'name': "Learn Pyhton 3"},
]


def home(request):
    return render(request, 'home.html', {'rooms':rooms})


def room(request):
    return render(request, 'room.html')
