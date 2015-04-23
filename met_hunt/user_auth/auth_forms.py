"""
User authenticating related form.
"""


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from user_auth.models import UserInfo

class RegisterForm(forms.Form):
	"""
	RegisterForm
	"""
	user_name = forms.CharField(label = "User Name", max_length = 30)
	password = forms.CharField(label = "Password", widget = forms.PasswordInput(), max_length = 50)
	first_name = forms.CharField(label = "First_Name", max_length = 50, required=False)
	last_name = forms.CharField(label = "Last Name", max_length = 50, required=False)
	email_address = forms.EmailField(label = "Email", max_length = 50, required=False)

	def register_form(self):
		# Use form.cleaned_data to save the user information.
		# ...
		# data = form.cleaned_data
		# Access user name using data['user_name'], password using data['password']
		# and email using data['email_address']. See auth_forms.py
		user = User.objects.create_user(username = self.cleaned_data['user_name'],
										password = self.cleaned_data['password'],
										first_name = self.cleaned_data['first_name'],
										last_name = self.cleaned_data['last_name'],
										email = self.cleaned_data['email_address'])

		# create empty userinfo
		user_info = UserInfo.objects.create(user=user)

		user.save()
		user_info.save()
	

class LogInForm(forms.Form):
	"""
	Creating user login form that will be used in login template page.
	"""

	user_name = forms.CharField(max_length=50, label = "User Name")
	password = forms.CharField(max_length = 50, 
							   label = "Password", 
							   widget = forms.PasswordInput())

	def login_process(self, request):
		user_name = self.cleaned_data['user_name']
		password = self.cleaned_data['password']

		# instanciate the user object.
		user = authenticate(username = user_name, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return user
		return None


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

		return user