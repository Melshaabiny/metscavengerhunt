"""
    The functions in this views.py render every html page throughout a user's hunt progress.
    It starts from the selection of a hunt from the categories list to the Rate Hunt page.
"""
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from hunts.models import set_ItemsData, set_HuntsData, pop_item, verify_id, init_huntprog, update_cur_item
from django.core.context_processors import csrf
from hunts.models import Hunts
global TEMP
global glob_hunt_id

def render_hunt(request, given_id):
    """
        :param: HttpRequest, interger id
        :rtype: HttpResponse
        This function gets triggered with the appropriate hunt id once a user chooses
        hunt from the categories page. It sets the hunt's data (title and starting location),
        and stores the items data in global var TEMP list.
        Finally, it renders the hunt's welcome page.
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
    return render_to_response("hunts/hunt.html", {"title": hunt_title, "start_pt": hunt_start, "user": request.user})

def next_proc(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse    
        If the current item is the last one in the hunt, next_proc() redirect to render_congrats
        Otherwise, it calls pop_item() to update the global list of items and redirects to render_clue()
    """
    global TEMP
    TEMP = pop_item(TEMP)
    if len(TEMP) > 0:
        return redirect('rend_clue')
    else:
        return redirect('rend_congrats')

def render_clue(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse        
        render item's clue page using global var item_clue as template variable
    """
    global TEMP
    return render_to_response("hunts/clue.html", {"clue_text":TEMP[0][1]})

def render_result(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse
        Based on the user input it either redirects to render_correct(),
        render_incorrect(), or render_congrats
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
        :param: HttpRequest
        :rtype: HttpResponse
        Render item's hint page with the appropriate hint crop and hint text.
    """
    global TEMP
    return render_to_response("hunts/hint.html", {"hint_text":TEMP[0][3], "hint_crop":TEMP[0][6]})

def render_verify(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse
        Renders item's verify page allowing the user to verify the item's ids.
    """
    c_srf = {}
    c_srf.update(csrf(request))
    return render_to_response("hunts/verify.html", c_srf, {})

def render_correct(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse
        Render the correct answer's page with some fun facts and the item's image.
    """
    global TEMP
    global glob_hunt_id
    num = TEMP[0][2]
    uname = request.user.username
    update_cur_item(glob_hunt_id, uname, num)
    return render_to_response("hunts/correct.html", {"url":TEMP[0][4], "fact":TEMP[0][5]})

def render_incorrect(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse        
        Render incorrect answer's page allwoing the user to retry.
    """
    return render_to_response("hunts/incorrect.html", {})

def render_congrats(request):
    """
        :param: HttpRequest
        :rtype: HttpResponse
        Render congratulations page after finishing hunt.
    """
    return render_to_response("hunts/congrats.html", {})


def hunt_detail(request, category):
    """
        :param: HttpRequest, String Category
        :rtype: HttpResponse     
        This view renders the page for each type of hunts available. It will
        contain the list of hunts in each category. And each of this list will 
        be linked to corresponding hunt page. Here, type will be a string that
        represent the type of hunt.
    """

    # get all hunts with Category == type.
    # try:
    # hunts = Hunt.objects.all(Category=type)
    if category == "Ancient":
        category = category + " Art"
    elif category == "Medieval":
        category = category + " Art"
    hunts = Hunts.objects.all().filter(Category=category)
    args = {'hunts' : hunts, 'title' : category + ' Collection', 'user':request.user}
    # except:
    #     args = {}

    return render_to_response('hunts/hunt_detail.html', args)
