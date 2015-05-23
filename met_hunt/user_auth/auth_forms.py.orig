from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
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

		# save it
		user.save()
		return

