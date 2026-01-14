from django.shortcuts import render


def home(req):
    return render(req, 'home.html')



def room(req, room_name):
    username = req.GET.get("username", "Guest")  # get username from query string
    return render(req, 'room.html', {
        "roomname": room_name,
        "username": username
    })

