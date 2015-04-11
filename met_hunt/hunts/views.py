from django.shortcuts import render_to_reponse
from hunts.models import Hunts, Items, Has

TEMP 		= []
item_clue	= ""
item_id 	= NULL
hunt_title	= ""
hunt_start 	= ""

'''
	* Gets triggered with the appropriate hunt_id once a user chooses a hunt from the categories drop down menu
	* Assigns hunt title and hunt id to their global vars
	* Creates a list of item objects and stores them into the TEMP global var
	* Redirects to the hunt.html page
'''
def getData(request, hunt_id):

	hunt_title 	= Hunts.objects.get(ID = hunt_id)
	hunt_start	= hunt_title.Start

	# List of items in a hunt. Instance of 'Has' class
	hunt_items 	= Has.objects.filter(hunt = hunt_title)
	# TODO TEMP should be a dic
	for x in range(0,hunt_items.count()):
		TEMP.append(hunt_items[x])
	
	# TODO
	# assign_vars()
	# redirect to render_hunt 

'''
	* Usign the TEMP global list, assing_vars() assigns the id and clue 
		of the first item in the list to their global vars
	* deletes (pops) the first item of the list

'''
def assing_vars():
	item_id 	= TEMP[0].item.ID
	item_clue 	= TEMP[0].clue

	del TEMP[0]
''' 
	* If the current item is the last one in the hunt, next_proc() redirect to render_congrats
	* Otherwise, it calls assing_vars() to update the item global vars 
		and redirects to render_clue()
'''
def next_proc():
	if len(TEMP) > 0:
		assing_vars()
	 	# TODO
	 	# redirect to render_clue()
	# else:
		#redirect to render_congrats()
'''
	* Checks the user input against the item id and returns a boolean result
'''
def verify_ID(usr_input):
	if usr_input == item_id:
		return True
	else:
	 	return False
'''
	* Funtions to render appropriate html files based on the user's progress
'''
def render_hunt(request):
	return render_to_reponse("hunts/hunt.html", {"title": hunt_title, "start_pt": hunt_start})

def render_clue(request):
	return render_to_reponse("hunts/clue.html", {"clue_text":item_clue})

def render_verify(request):
	return render_to_reponse("hunts/verify.html", {})

# TODO write the html files: correct.html and incorrect.html
def render_result(request, usr_input):
	if verify_ID(usr_input) == True:
		# redirect to correct page
		return render_to_reponse("hunts/correct.html", {})
	else:
		# or to incorrect page
		return render_to_reponse("hunts/incorrect.html", {})

def render_congrats(request):
	return render_to_reponse("hunts/congrats.html", {})
