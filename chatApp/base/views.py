from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

def home(request): #query comes with request
    q= request.GET.get('q') if request.GET.get('q') != None else ""
    rooms= Room.objects.filter(#query matches any of three name, description, topic name
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )
    topics= Topic.objects.all()
    room_count= rooms.count()

    context= {'rooms': rooms, 'topics':topics, 'room_count': room_count}#dictionary to send arrays, dictionaries, objects, etc as response
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context= {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form=RoomForm()#a form
    if request.method == 'POST':
        form= RoomForm(request.POST)#form as instance of Room class
        if form.is_valid():
            form.save()
            return redirect('home')
    context= {'form': form}
    return render(request, 'base/room_form.html', context)
# When user clicks create form, a specific url is accessed and we send back a form. (Form will get submitted to this same url)
# form is not the instance of class Room. 
# the request comes and we have to make form as instance so pass request to RoomForm

def updateRoom(request, pk):
    room= Room.objects.get(id=pk)
    form= RoomForm(instance=room)#pre filled values in the form with values of room with id pk
    if request.method == 'POST':
        form= RoomForm(request.POST, instance=room)#update room, dont create new room
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

# to update a room we present user with a form

def deleteRoom(request, pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})