from django.shortcuts import render_to_response
from django.shortcuts import redirect
from hunts.models import Hunts, Items, Has, set_ItemsData, set_HuntsData, pop_item, verify_id
from django.core.context_processors import csrf

#global TEMP

def render_hunt(request, id):
	"""
        * Gets triggered with the appropriate hunt id once a user chooses
        * a hunt from the categories' drop down menu
        * Sets the hunt's data (title and starting location) and stores the items data in global var TEMP list 
        * finally, it renders the welcome page 
    """
	global temp
	hunt_dict = set_HuntsData(id)
	temp = set_ItemsData(id)
	return render_to_response("hunts/hunt.html", {"title": hunt_dict['hunt title'], "start_pt": hunt_dict['hunt start']})

def next_proc(request):
    """
        * If the current item is the last one in the hunt, next_proc() redirect to render_congrats
        * Otherwise, it calls pop_item() to update the global list of items
        	and redirects to render_clue()
    """
    global temp
    temp = pop_item(temp)
    if len(temp) > 0:
        return redirect('rend_clue')

def render_clue(request):
    """
        * render item's clue page using global var item_clue as template var
    """
    global temp
    return render_to_response("hunts/clue.html", {"clue_text":temp[0][1]})


def render_result(request):
    """
        * based on the user input it either redirects to render_correct(), render_incorrect(), or render_congrats
    """
    if request.method == "POST":
        
        usr_input_value = str(request.POST.get('input', ''))
        
        if verify_id(usr_input_value) == True:
            global temp
            if len(temp)==1:
                return redirect('rend_congrats')
            else:
                return redirect('rend_correct')
        else:
            return redirect('rend_incorrect')

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
    return render_to_response("hunts/correct.html", {})

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
