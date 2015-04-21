from django.shortcuts import render_to_response, redirect
from forum.models import Thread, QuestionAsked
from django.http import JsonResponse

# Create your views here.

def thread_main(request):
	"""
	This views.py is responsible for the view of main thread page. It should display
	all type of threads with their description and total number of posts in each thread.
	"""
	threads = Thread.objects.all()
	args = {'threads':threads}
	return render_to_response('forum/thread_main.html', args)

def modern_thread(request):
	thread = Thread.objects.get(type='modern')
	args = {'total_post' : thread.total_post}
	return render_to_response('forum/modern_thread.html', args)

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
							  'username' : each.user.username,
							  'picture' : each.user.userinfo.picture.path}]

		return JsonResponse(data)