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

	def register_user(self):
		"""
		This member function **register_user** takes care of registering the visitor's user
		information into the database.
		"""

		# register the user using User model.
		user_name = self.cleaned_data['user_name']
		user_password = self.cleaned_data['password']
		user_first_name = self.cleaned_data['first_name']
		user_last_name = self.cleaned_data['last_name']
		user_email = self.cleaned_data['email_address']

		user = User.objects.create_user(username = user_name,
										password = user_password,
										first_name = user_first_name,
										last_name = user_last_name,
										email = user_email)

		# create empty user info.
		user_info = UserInfo.objects.create(user=user)

		# save.
		user.save()
		user_info.save()
		return

class LogInForm(forms.Form):
	"""
	Creating user login form that will be used in login template page.
	"""

	user_name = forms.CharField(max_length=50, label = "User Name")
	password = forms.CharField(max_length = 50, 
							   label = "Password", 
							   widget = forms.PasswordInput())

	def log_user_in(self, request):
		"""
		This member function can take care of the process of loggin the user in.
		"""

		user_name = self.cleaned_data['user_name']
		password = self.cleaned_data['password']

		# instanciate the user object.
		user = authenticate(username = user_name, password = password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return user

		return None

