"""
user_auth.views

	This views.py is responsible for all user authenticating related jobs such as login a user,
	register a visitor...
"""
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from user_auth.auth_forms import RegisterForm, LogInForm, EditForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf # for Cross Site Request Forgery.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from user_auth.models import UserInfo

variable = 123

@login_required
def edit(request):
	"""
	The user can edit their information from the profile page.
	"""
	form = None
	title = "Edit User Information"
	if request.method == 'POST':
		# make changes.
		form = EditForm(request.POST, request.FILES)
		if form.is_valid():
			# form.process(request.user)
			if form.cleaned_data['first_name']:
				request.user.first_name = form.cleaned_data['first_name']
			if form.cleaned_data['last_name']:
				request.user.last_name = form.cleaned_data['last_name']
			if form.cleaned_data['picture']:
				print 'called'
				user_info = UserInfo.objects.get(user = user)
				user_info.picture = form.cleaned_data['picture']
				user_info.save()

			request.user.save()
			args = {'editted':True, 'user':request.user}
			args.update(csrf(request))
			return render_to_response('user_auth/edit.html', args)
	else:
		# provide edit form.
		form = EditForm()
	args = {'form':form, 'user':request.user, 'title':title, 'editted':False}
	args.update(csrf(request))
	return render_to_response('user_auth/edit.html', args)

@login_required	
def profile(request):
	user = None
	if request.user.is_authenticated():
		user = request.user

	args = {'user':user}
	args.update(csrf(request))
	return render_to_response('user_auth/profile.html', args)

# Create your views here.
def login_user(request):
	"""
	login a user into the website.
	"""
	title = "LogIn"
	args = {}
	user = None

	if request.method == "POST":
		# The method should be post since it does not expose the user imformation on url.
		# it should be get method since login does not change state of any user data.
		form = LogInForm(request.POST)
		# check the form validation.
		if form.is_valid():

			user_name = form.cleaned_data['user_name']
			password = form.cleaned_data['password']

			# instanciate the user object.
			user = authenticate(username = user_name, password = password)

			if user is not None:
				if user.is_active:
					login(request, user)

			args = {'user':user}
			args.update(csrf(request))
			return render_to_response('home/home.html', args)
	else:
		form = LogInForm()


	args = {'form':form, 'title':title}
	args.update(csrf(request))
	return render_to_response('user_auth/login.html', args)

@login_required
def logout_user(request):
	logout(request)
	return render_to_response('home/home.html', {})

def register(request):
	"""
	Register new user. If the request method is not POST, then return the register page template.
	Otherwise, register the user with given data.
	"""
	user = None
	
	# handles registering.
	title = 'Register'
	args = {}
	if request.method == 'POST':
		# it means that we received inputs from the user.
		# Then, fill them out.
		form = RegisterForm(request.POST)
		# check if all inputs are valid.
		if form.is_valid():
			# Use form.cleaned_data to save the user information.
			# ...
			# data = form.cleaned_data
			# Access user name using data['user_name'], password using data['password']
			# and email using data['email_address']. See auth_forms.py
			user = User.objects.create_user(username = form.cleaned_data['user_name'],
											password = form.cleaned_data['password'],
											first_name = form.cleaned_data['first_name'],
											last_name = form.cleaned_data['last_name'],
											email = form.cleaned_data['email_address'])

			# create empty userinfo
			user_info = UserInfo.objects.create(user=user)

			user.save()
			user_info.save()
			return HttpResponseRedirect('/')
		else:
			# form is not valid.
			args = {'title':'Data is not valid', 'valid':False}
			return render_to_response('user_auth/register.html', args)
	else:
		form = RegisterForm()

	args = {'form' : form, 
			'title' : title,
			'valid':True}
	args.update(csrf(request)) # Guess passing csrf token to the template.
	return render_to_response('user_auth/register.html', args)
