from django.shortcuts import render
from django.shortcuts import render_to_response
def verf_clue(request):
	#jlkjdflkjfsfsad
	return render_to_response("tutorial_hunt/verify.html", {})

def rend_welcome(request):
	return render_to_response("tutorial_hunt/tutorial.html",{})

def rend_clue(request):
        return render_to_response("tutorial_hunt/clues.html",{})

