# from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from hunts.models import Hunts, Items, Has

'''
	* Gets triggered with the appropriate hunt_id once a user chooses a hunt from the categories' drop down menu
	* Assigns hunt title and hunt id to their global vars
	* Creates a list of item objects and stores them into the TEMP global var
	* Redirects to the hunt.html page
'''
def getData(request):
	
	global hunt_title, hunt_start, TEMP

	hunt 		= Hunts.objects.get(ID = 001)
	hunt_title	= str(hunt.Title)
	hunt_start	= str(hunt.Start)

	# List of items in a hunt. Instance of 'Has' class
	hunt_items 	= Has.objects.filter(hunt_id = 001)
	
	tuples = ()
	for x in range(0,hunt_items.count()):
		tuples = tuples + ((str(hunt_items[x].item.ID), str(hunt_items[x].clue), int(hunt_items[x].number)),)
	
	# sort using the order number of each item
	TEMP = sorted(list(tuples), key = lambda element: element[2])
	assign_vars()
	
	return redirect('hunt_welcome')
	#return render_hunt(request,title = hunt_title, start = hunt_start)
'''
	* Usign the TEMP global list, assign_vars() assigns the id and clue 
		of the first item in the list to their global vars
	* deletes (pops) the first item of the list
'''
def assign_vars():

	global TEMP, item_id, item_clue
	
	item_id 	= TEMP[0][0]
	item_clue 	= TEMP[0][1]

	del TEMP[0]
''' 
	* If the current item is the last one in the hunt, next_proc() redirect to render_congrats
	* Otherwise, it calls assign_vars() to update the item global vars 
		and redirects to render_clue()
'''
def next_proc():
	global TEMP
	if len(TEMP) > 0:
		assign_vars()
	 	return redirect('rend_clue')
	else:
		return redirect('rend_congrats')
'''
	* Checks the user input against the item id and returns a boolean result
'''
def verify_ID(usr_input):
	global item_id
	if usr_input == item_id:
		return True
	else:
	 	return False
'''
	* Funtions to render appropriate html files based on the user's progress
'''

def render_hunt(request):
	global hunt_title, hunt_start
 	return render_to_response("hunts/hunt.html", {"title": hunt_title, "start_pt": hunt_start})

def render_clue(request):
	global item_clue
	return render_to_response("hunts/clue.html", {"clue_text":item_clue})

def render_verify(request):
	return render_to_response("hunts/verify.html", {})

def render_correct(requst):
	return render_to_response("hunts/correct.html",{})

def render_incorrect(request):
	return render_to_response("hunts/incorrect.html", {})

def render_result(request):
	#USE SESSIONS TO GET DATA FROM FORM
	if verify_ID(usr_input) == True:
		return redirect('rend_correct')
	else:
		return redirect('rend_incorrect')

def render_congrats(request):
	return render_to_response("hunts/congrats.html", {})
