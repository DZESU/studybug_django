from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
rooms = [

    {'id': 1, 'name': "Learn Pyhton 1"},
    {'id': 2, 'name': "Learn Pyhton 2"},
    {'id': 3, 'name': "Learn Pyhton 3"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'room.html')
