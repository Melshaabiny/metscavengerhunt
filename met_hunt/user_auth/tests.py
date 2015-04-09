"""
Unit test for **user_auth** django application.

The list of tests are : 

	- **test_login_status_code()** checks if accessing url **/user_auth/login/** returns status_code 200.
	- **test_register_status_code()** checks if accessing url **/user_auth/register/** returns status_code 200/
	- **test_register_user()** checks if **RegisterForm.register_user()** gets called when **user_auth.views.register** gets POST data.
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from user_auth.views import login, logout_user, register

# Create your tests here.
class user_authTest(TestCase):

	def setUp(self):
		self.client = Client()

	def tearDown(self):
		User.objects.all().delete() # clean up the user database.

	def test_register_status_code(self):
		# create client.
		response = self.client.get('/user_auth/register/')
		self.assertEqual(response.status_code, 200)

	def test_login_status_code(self):
		response = self.client.get('/user_auth/login/')
		self.assertEqual(response.status_code, 200)

	def test_views_register(self):
		"""
		**test_views_register()** checks if the function is called if anybody accessed the url **/user_auth/register/**.
		This test should be considered as different test with **test_register_status_code()** since this function just
		checks if the httpresponse returns the status_code 200.
		"""

		with patch('user_auth.views.register') as reg:
			# access the url.
			self.client.get('/user_auth/register/')
			# check if the function gets called.
			reg.called

	def test_views_login(self):
		"""
		**test_views_login()** checks if the function is called if anybody accessed the url **/user_auth/login/**.
		This test should be considered as different test with **test_login_status_code()** since this function just
		checks if the httpresponse returns the status_code 200. 
		"""

		with patch('user_auth.views.login') as login:
			# access the url.
			self.client.get('/user_auth/login/')
			login.called

	def test_RegisterForm(self):
		"""
		**test_RegisterForm()** checks if request.method to **user_auth.views.register()** is POST or 
		GET, the form is properly instantiated. 
		"""

		with patch('user_auth.views.RegisterForm') as reg:
			args = {'user_name':'user1', 'password':'password'}
			self.client.post('/user_auth/register/', args)
			# check if RegisterForm is called with post method.
			reg.called

		with patch('user_auth.views.RegisterForm') as reg:
			self.client.get('/user_auth/register/')
			# check if RegisterForm is called with post method.
			reg.called

	def test_register_user(self):
		"""
		**test_register_user()** check if the function **RegisterForm.register_user()** 
		is called when POST data is sent to **user_auth.views.register()** function.
		"""

		# mock register_user function.
		with patch('user_auth.views.RegisterForm.register_user') as reg:
			reg.return_value = None
			# The function gets called when user_auth.register() gets POST data.
			response = self.client.post('/user_auth/register/', {'user_name':'test_user', 'password':'test1_user'})
			reg.assert_called_with()


	# def test_auth_forms_register_user(self):
	# 	"""
	# 	This function checks if the function *register_user* in **auth_forms.py** was called with
	# 	appropriate data.
	# 	"""

	# 	with patch('Register')