from django.shortcuts import render_to_response
from django.shortcuts import redirect
#from cr_hunt.models import 
from django.core.context_processors import csrf
# Create your views here.

from .forms import ItemForm

def render_main(request):
    return render_to_response("cr_hunt/cr_hunt_main.html")

def render_ats(request):
    c_srf = {}
    c_srf.update(csrf(request))
    return render_to_response("cr_hunt/cr_hunt_title_strt.html", c_srf, {})

#def render_aitem(request):
#    c_srf = {}
#    c_srf.update(csrf(request))
#    return render_to_response("cr_hunt/cr_hunt_aitem.html",c_srf, {})

def render_proc_ts(request):
    pass
