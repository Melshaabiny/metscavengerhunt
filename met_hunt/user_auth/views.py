"""
user_auth.views

	This views.py is responsible for all user authenticating related jobs such as login a user,
	register a visitor...
"""

from django.shortcuts import render_to_response
from user_auth.auth_forms import RegisterForm, LogInForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf # for Cross Site Request Forgery.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def login(request):
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
			user = form.log_user_in(request)
			args = {'user':user}
			return render_to_response('home/home.html', args)
	else:
		form = LogInForm()


	args = {'form':form, 'title':title}
	args.update(csrf(request))
	return render_to_response('auth/login.html', args)

@login_required
def logout_user(request):
	logout(request)
	return render_to_response('home/home.html', {})

def register(request):
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
			form.register_user()
			# print User.objects.get_queryset()
			return HttpResponseRedirect('/')
	else:
		form = RegisterForm()

	args = {'form' : form, 
			'title' : title,}
	args.update(csrf(request)) # Guess passing csrf token to the template.
	return render_to_response('auth/register.html', args)