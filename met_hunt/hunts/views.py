"""
    * views functions that renders each html throughout a user's hunt progress
    * starts from the selection of a hunt from the categories list to the Rate Hunt page
"""
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from hunts.models import set_ItemsData, set_HuntsData, pop_item, verify_id, init_huntprog, update_cur_item
from django.core.context_processors import csrf

global TEMP
global glob_hunt_id

def render_hunt(request, given_id):
    """
        * gets triggered with the appropriate hunt id once a user chooses
        * a hunt from the categories' drop down menu
        * sets the hunt's data (title and starting location)
        * stores the items data in global var TEMP list
        * finally, it renders the welcome page
    """
    global TEMP
    global glob_hunt_id
    glob_hunt_id = given_id
    hunt_dict = set_HuntsData(given_id)
    TEMP = set_ItemsData(given_id)
    hunt_title = hunt_dict['hunt title']
    hunt_start = hunt_dict['hunt start']
    uname = request.user.username
    init_huntprog(given_id, uname)
    return render_to_response("hunts/hunt.html", {"title": hunt_title, "start_pt": hunt_start})

def next_proc(request):
    """
        * If the current item is the last one in the hunt, next_proc() redirect to render_congrats
        * Otherwise, it calls pop_item() to update the global list of items
            and redirects to render_clue()
    """
    global TEMP
    TEMP = pop_item(TEMP)
    if len(TEMP) > 0:
        return redirect('rend_clue')
    else:
        return redirect('rend_congrats')

def render_clue(request):
    """
        * render item's clue page using global var item_clue as TEMPlate var
    """
    global TEMP
    return render_to_response("hunts/clue.html", {"clue_text":TEMP[0][1]})


def render_result(request):
    """
        * based on the user input it either redirects to render_correct(),
        * render_incorrect(), or render_congrats
    """
    if request.method == "POST":

        usr_input_value = str(request.POST.get('input', ''))

        if verify_id(usr_input_value) == True:
            global TEMP
            if len(TEMP) == 0:
                return redirect('rend_congrats')
            else:
                return redirect('rend_correct')
        else:
            return redirect('rend_incorrect')

def render_hint(request):
    """
        * render item's hint page
    """
    global TEMP
    return render_to_response("hunts/hint.html", {"hint_text":TEMP[0][3], "hint_crop": TEMP[0][6]})

def render_verify(request):
    """
        * render item's verify page
    """
    c_srf = {}
    c_srf.update(csrf(request))
    return render_to_response("hunts/verify.html", c_srf, {})

def render_correct(request):
    """
        * render correct answer's page
    """
    global TEMP
    global glob_hunt_id
    num = TEMP[0][2]
    uname = request.user.username
    update_cur_item(glob_hunt_id, uname, num)
    return render_to_response("hunts/correct.html", {"url":TEMP[0][4], "fact":TEMP[0][5]})

def render_incorrect(request):
    """
        * render incorrect answer's page
    """
    return render_to_response("hunts/incorrect.html", {})

def render_congrats(request):
    """
        * render congratulations page after finishing hunt
    """
    return render_to_response("hunts/congrats.html", {})
