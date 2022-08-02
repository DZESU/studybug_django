from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.
# rooms = [
#     {'id': 1, 'name': "Learn Pyhton 1"},
#     {'id': 2, 'name': "Learn Pyhton 2"},
#     {'id': 3, 'name': "Learn Pyhton 3"},
# ]


def home(request:HttpRequest):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains = query) | Q(name_icontain = query) | Q(description_icontain = query))
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {"room": room}
    return render(request, 'room.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})