from django.shortcuts import render_to_response, redirect
from forum.models import Thread
# Create your views here.

def thread_main(request):
	"""
	This views.py is responsible for the view of main thread page. It should display
	all type of threads with their description and total number of posts in each thread.
	"""
	threads = Thread.objects.all()
	args = {'threads':threads}
	return render_to_response('forum/thread_main.html', args)
