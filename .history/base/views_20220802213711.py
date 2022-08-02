from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.
# rooms = [
#     {'id': 1, 'name': "Learn Pyhton 1"},
#     {'id': 2, 'name': "Learn Pyhton 2"},
#     {'id': 3, 'name': "Learn Pyhton 3"},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {"room":room}
    return render(request, 'room.html', context)


def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)
