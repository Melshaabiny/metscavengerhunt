from django.shortcuts import render_to_response
from django.shortcuts import redirect
from hunts.models import Hunts, Items, Has
from django.core.context_processors import csrf

# TEMP = []
# item_id = 0
# item_clue = ""
# hunt_title = ""
# hunt_start = ""

def get_data(request):
    '''
    * Gets triggered with the appropriate hunt_id once a user chooses
    * a hunt from the categories' drop down menu
    * Assigns hunt title and hunt id to their global vars
    * Creates a list of item objects and stores them into the TEMP global var
    * Redirects to the hunt.html page
    '''
    global hunt_title, hunt_start, TEMP

    hunt = Hunts.objects.get(ID=001)
    hunt_title = str(hunt.Title)
    hunt_start = str(hunt.Start)

    #List of items in a hunt. Instance of 'Has' class
    hunt_items = Has.objects.filter(hunt_id=001)
    tuples = ()
    for x in range(0, hunt_items.count()):
        tuples = tuples + ((str(hunt_items[x].item.ID), str(hunt_items[x].clue), int(hunt_items[x].number)),)
    
    # sort using the order number of each item
    TEMP = sorted(list(tuples), key=lambda element: element[2])
    assign_vars()
    return redirect('hunt_welcome')
    #return render_hunt(request,title = hunt_title, start = hunt_start)

def assign_vars():
    '''
        * Usign the TEMP global list, assign_vars() assigns the id and clue 
            of the first item in the list to their global vars
        * deletes (pops) the first item of the list
    '''
    global TEMP, item_id, item_clue
    item_id = TEMP[0][0]
    item_clue = TEMP[0][1]
    del TEMP[0]

def verify_id(usr_input):
    '''
        * Checks the user input against the item id and returns a boolean result
    '''
    global item_id
    if usr_input == item_id:
        return True
    else:
        return False

def next_proc(request):
    ''' 
        * If the current item is the last one in the hunt, next_proc() redirect to render_congrats
        * Otherwise, it calls assign_vars() to update the item global vars 
            and redirects to render_clue()
    '''
    global TEMP
    if len(TEMP) > 0:
        assign_vars()
        return redirect('rend_clue')
    else:
        return redirect('rend_congrats')

def render_hunt(request):
    '''
        * render hunt welcome page
    '''
    global hunt_title, hunt_start
    return render_to_response("hunts/hunt.html", {"title": hunt_title, "start_pt": hunt_start})

def render_clue(request):
    '''
        * render item's clue page 
    '''    
    global item_clue
    return render_to_response("hunts/clue.html", {"clue_text":item_clue})

def render_verify(request):
    '''
        * render item's verify page
    '''
    c_srf = {}
    c_srf.update(csrf(request))
    return render_to_response("hunts/verify.html", c_srf, {})

def render_result(request):
    '''
        * render result of user's input
    '''
    if request.method == "POST":
        
        usr_input_value = str(request.POST.get('input', ''))
        
        if verify_id(usr_input_value) == True:
            return redirect('rend_correct')
        else:
            return redirect('rend_incorrect')

def render_correct(request):
    '''
        * render correct answer's page
    '''
    return render_to_response("hunts/correct.html", {})

def render_incorrect(request):
    '''
        * render incorrect answer's page
    '''    
    return render_to_response("hunts/incorrect.html", {})

def render_congrats(request):
    '''
        * render congratulations page after finishing hunt
    '''   
    return render_to_response("hunts/congrats.html", {})
