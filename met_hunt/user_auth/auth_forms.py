"""
User authenticating related form.
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from user_auth.models import UserInfo

class RegisterForm(forms.Form):
	"""
	"""
	user_name = forms.CharField(label = "User Name",
						  		max_length = 30)

	password = forms.CharField(label = "Password",
							   widget = forms.PasswordInput(),
							   max_length = 50)

	first_name = forms.CharField(label = "First_Name",
								 max_length = 50, required=False)

	last_name = forms.CharField(label = "Last Name",
								max_length = 50, required=False)

	email_address = forms.EmailField(label = "Email",
							   		 max_length = 50, required=False)

	

class LogInForm(forms.Form):
	"""
	Creating user login form that will be used in login template page.
	"""

	user_name = forms.CharField(max_length=50, label = "User Name")
	password = forms.CharField(max_length = 50, 
							   label = "Password", 
							   widget = forms.PasswordInput())


class EditForm(forms.Form):
	"""
	**EditForm** is responsible for editing the user information. The assumption is that the user
	is already registered. We restrict non-registered user to access edit page from the profifle
	views function. The list of information that the user can edit is : 

		- Password
		- Description
		- Picture
		- Name
	"""
	picture = forms.ImageField(required = False)
	first_name = forms.CharField(max_length = 50, required = False)
	last_name = forms.CharField(max_length = 50, required = False)
	password = forms.CharField(max_length = 50, widget = forms.PasswordInput(), required = False)
	description = forms.CharField(widget = forms.Textarea, required = False)

	def process(self, user):
		if self.cleaned_data['first_name']:
			user.first_name = self.cleaned_data['first_name']
		if self.cleaned_data['last_name']:
			user.last_name = self.cleaned_data['last_name']
		if self.cleaned_data['picture']:
			user_info = UserInfo.objects.get(user = user)
			user_info.picture = self.cleaned_data['picture']
			user_info.save()
		user.save()