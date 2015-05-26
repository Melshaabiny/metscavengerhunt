"""
    The functions in this views.py render every html page throughout a user's create hunt progress.
    It starts from the adding a hunt title and starting location
    to selecting items from our database of all items.
"""
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from cr_hunt.models import add_hunt_its, add_hunt_has, gen_hunt_id, get_cur_count
from django.core.context_processors import csrf

from .forms import ItemForm
global hunt_id
global i_counter

def render_main(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest    
        Renders the welcome page for the create hunt app.
    """    
    if request.user.is_authenticated():
        global hunt_id
        hunt_id = request.user.username
        hunt_id = gen_hunt_id(hunt_id)
        global i_counter
        i_counter = get_cur_count(hunt_id)
        return render_to_response("cr_hunt/cr_hunt_main.html")
    else:
        return redirect('cr_error')

def render_ats(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest
        Renders the page that allows the user to input his hunt title and starting location.
    """
    if request.user.is_authenticated():
        c_srf = {}
        c_srf.update(csrf(request))
        return render_to_response("cr_hunt/cr_hunt_title_strt.html", c_srf, {})
    else:
        return redirect('cr_error')

def render_aitem(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest
        Renders the add item page, where the user is prompt to select items from our database,
        (the Met's database, ultimately) and add it to the hunt that they're creating.
    """
    if request.user.is_authenticated():
        form = ItemForm()
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid:
                pass
        c_srf = {"form": form}
        c_srf.update(csrf(request))
        return render_to_response("cr_hunt/cr_hunt_aitem.html", c_srf)
    else:
        return redirect('cr_error')

def render_end(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest    
        Renders the end page for the create hunt app.
    """
    return render_to_response("cr_hunt/cr_hunt_end.html")

def render_proc_ts(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest
        Renders the "Next" page that allows the user to input his hunt title and starting location.
    """
    if request.user.is_authenticated():
        if request.method == "POST":
            global hunt_id
            uname = request.user.username
            title = str(request.POST.get('title', ''))
            start = str(request.POST.get('start', ''))
            add_hunt_its(hunt_id, title, start, uname)
            return redirect('cr_aitem')
    else:
        return redirect('cr_error')

def render_proc_it(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest
        Renders the "Next" add item page, where the user is prompt to select items from our database,
        (the Met's database, ultimately) and add it to the hunt that they're creating.
    """
    if request.user.is_authenticated():
        global i_counter
        if i_counter == 10:
            return redirect('cr_end')
        if request.method == "POST":
            global hunt_id
            global i_counter
            clue = str(request.POST.get('clue', ''))
            item_id = str(request.POST.get('item', ''))
            i_counter = i_counter + 1
            return redirect('cr_aitem')
    else:
        return redirect('cr_error')

def render_error(request):
    """
        :param: HttpRequest
        :rtype: HttpRequest
        Renders the error page for the create hunt app.
    """
    return render_to_response("cr_hunt/cr_hunt_error.html")
