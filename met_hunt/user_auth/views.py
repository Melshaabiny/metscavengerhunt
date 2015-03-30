from django.shortcuts import render_to_response
from user_auth.auth_forms import RegisterForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf # for Cross Site Request Forgery.

# Create your views here.
def login(request):
	return render_to_response('auth/login.html', {})


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
