from django.shortcuts import render_to_response, redirect
from forum.models import Thread, QuestionAsked
from django.http import JsonResponse

# Create your views here.

def thread_layout(request):
	"""
	This views.py is responsible for the view of main thread page. It should display
	all type of threads with their description and total number of posts in each thread.
	"""
	return render_to_response('forum/thread_layout.html')

def modern(request):
	return render_to_response('forum/modern.html')

def load_data(request):
	if request.method == "GET":
		# instantiate the thread.
		thread = Thread.objects.get(type="modern")
		posts = QuestionAsked.objects.filter(thread=thread)
		########## The json file always formatted as 
				   # {
				   # 'data' : [
				   # 			 {'component':'value'}, ...
				   # ]
				   # }
		data = {'json':[]}
		for each in posts:
			data['json'] += [{'title' : each.title,
							  'description' : each.description,
							  'when': each.when,
							  'view' : each.view,
							  'username' : each.user.username
							  }]
		return JsonResponse(data)