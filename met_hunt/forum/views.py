from django.shortcuts import render_to_response, redirect
from forum.models import Thread, QuestionAsked
from django.http import JsonResponse
from forum.models import Thread, QuestionAsked
from django.contrib.auth.models import User
import json

# Create your views here.

def thread_layout(request):
		"""
		This views.py is responsible for the view of main thread page. It should display
		all type of threads with their description and total number of posts in each thread.
		"""
		return render_to_response('forum/thread_layout.html')

def modern(request):
		return render_to_response('forum/modern.html')

def create(request):
		return render_to_response('forum/create_post.html')

def load_data(request):
	"""
	This function gets posts in the database and return it as json data.
	"""
	if request.method == "GET":
		# instantiate the thread.
		thread = Thread.objects.get(type="modern")
		posts = QuestionAsked.objects.filter(thread=thread).order_by('-when')
		########## The json file always formatted as 
							 # {
							 # 'data' : [
							 #             {'component':'value'}, ...
							 # ]
							 # }
		data = {'json':[]}
		for each in posts:
			data['json'] += [{'title' : each.title,
							'description' : each.description,
							'when': each.when,
							'view' : each.view,
							'username' : each.user.username,
							'thread' : 'modern',
							'logged_user' : request.user.username}]
		return JsonResponse(data)

def submit(request):
		"""
		This submit function takes the title and description of the post that
		a user creates, sent by angularjs with $http.post method. This function
		should handle data saving into thread model.
		"""
		data = json.loads(request.body)

		user = User.objects.get(username=data['username'])
		thread = Thread.objects.get(type=data['thread'])
		post = QuestionAsked.objects.create(user=user, thread=thread, title=data['title'], description=data['description'])
		return render_to_response('forum/modern.html')