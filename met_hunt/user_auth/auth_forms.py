from django import forms

class RegisterForm(forms.Form):
	user_name = forms.CharField(label = "User Name",
						  max_length = 30)

	password = forms.CharField(label = "Password",
							   widget = forms.PasswordInput(),
							 max_length = 50)

	email_address = forms.EmailField(label = "Email",
							   max_length = 50)

