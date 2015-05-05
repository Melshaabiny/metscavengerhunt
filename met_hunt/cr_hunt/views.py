from django.shortcuts import render_to_response
from django.shortcuts import redirect
from cr_hunt.models import add_hunt_its, add_hunt_has
from django.core.context_processors import csrf
# Create your views here.

from .forms import ItemForm
global hunt_id
global i_counter
def render_main(request):
    #if request.user.is_authenticated():
    #hunt_id = request.user.username
    #possible solution limit users to one hunt per day grab date as set of numbers attach to username for unique id
    global hunt_id
    hunt_id = 12349
    global i_counter
    i_counter = 0
    return render_to_response("cr_hunt/cr_hunt_main.html")

def render_ats(request):
    c_srf = {}
    c_srf.update(csrf(request))
    return render_to_response("cr_hunt/cr_hunt_title_strt.html", c_srf, {})

def render_aitem(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid:
            pass
    c_srf = {"form": form}
    c_srf.update(csrf(request))
    return render_to_response("cr_hunt/cr_hunt_aitem.html", c_srf)

def render_end(request):
    return render_to_response("cr_hunt/cr_hunt_end.html")

def render_proc_ts(request):
    if request.method == "POST":
        global hunt_id
        title = str(request.POST.get('title', ''))
        start = str(request.POST.get('start', ''))
        add_hunt_its(hunt_id, title, start)
        return redirect('cr_aitem')

def render_proc_it(request):
    if i_counter == 10:
        return redirect('cr_end')
    if request.method == "POST":
        global hunt_id
        global i_counter
        clue = str(request.POST.get('clue',''))
        item_id = str(request.POST.get('item',''))
        i_counter = i_counter + 1
        return redirect('cr_aitem')
