from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from kk.models import Rooms, AuthUser
from kk.web.forms import RoomForm

def home(request):
    rooms = Rooms.objects.all()
    users = AuthUser.objects.all()
    content = {
               'rooms' : rooms,
               'users' : users
               }
    return render_to_response('index.html', content)

def users(request):
    users = AuthUser.objects.all()
    return render_to_response('users.html', {'users' : users})

def rooms(request):
    rooms = Rooms.objects.all()
    return render_to_response('rooms.html', {'rooms' : rooms})

def create_room(request):    
    if request.POST:
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rooms/')
    else:
        form = RoomForm()
        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('create_room.html', args)

def create_user(request):
    return render_to_response('create_user.html')