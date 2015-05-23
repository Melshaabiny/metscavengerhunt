from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from home.models import get_leaderboard
from hunts.models import Hunts
import os

# Create your views here.
def main(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
    else:
        user = None
    ldr = get_leaderboard()
    args = {'user':user, 'ldr_brd' : ldr}
    return render_to_response('home/home.html', args)

def wiki(request):
    return render_to_response('html/index.html')

def search(request, query):
    # find from Hunts and Items
    lst = Hunts.objects.filter(Title__contains=query)
    args = {'data':lst}
    return render_to_response('home/search_template.html', args)
