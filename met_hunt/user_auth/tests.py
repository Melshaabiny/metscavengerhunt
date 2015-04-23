"""
Unit test for **user_auth** django application.

The list of tests are : 

	- **test_login_status_code()** checks if accessing url **/user_auth/login/** returns status_code 200.
	- **test_register_status_code()** checks if accessing url **/user_auth/register/** returns status_code 200/
	- **test_register_user()** checks if **RegisterForm.register_user()** gets called when **user_auth.views.register** gets POST data.
"""

from django.test import Client
from django.contrib.auth.models import User
from mock import MagicMock
from mock import Mock
from mock import patch
from user_auth.views import login_user, logout_user, register, profile, edit
from user_auth.models import UserInfo
from django.http import QueryDict
from django.utils.datastructures import MultiValueDict
import unittest
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class user_authTest(unittest.TestCase):
	def setUp(self):
		"""
		**setUp** method sets up all neccessary modules. djanfo.TestCase inherits unittest so it follows same syntax
		that the unittest libary use.
		"""
		self.client = Client()

	def tearDown(self):
		"""
		**teatDown** method removes all the changes that the test cases made for our system. This will be executed 
		each time that the test case runs.
		"""
		User.objects.all().delete() # clean up the user database.


###### Unit tests
#####################################################
####################register unit tests##############
	def test_unit_register_with_POST(self):
		"""
		We need to mock several things to make this unittest.

			1. request
			2. register_form() : For this, make seperate test.
				- request has **method** attribute that specifies the method of the form.
			3. Need to mock RegisterForm because we are not testing the register function.
				- RegisterForm instance should have is_valid() method that returns boolean.
			4. We need to mock HttpResponseRedirect.
		"""
		with patch('user_auth.views.RegisterForm') as form:
			with patch('user_auth.views.HttpResponseRedirect') as redir:
				request = MagicMock()
				request.method = "POST" ## this will pass if request.POST == "POST" part.
				request.POST = "some_input"
				form.return_value = Mock()
				form.return_value.is_valid = Mock(return_value=True)
				# mock register_form
				form.return_value.register_form = Mock(return_value=None)
				register(request)
				# make function call
				form.assert_called_with("some_input")
				redir.assert_called_with('/')
				self.assertTrue(form.return_value.register_form.called)

	def test_unit_register_with_invalidPOST(self):
		"""
		This function tests the **register()** function with invalid post data.
		we should mock

			1. request
			2. RegisterForm
				- is_valid()
			3. args
		"""

		with patch('user_auth.views.RegisterForm') as reg:
			request = MagicMock()
			request.method = "POST"
			request.POST = "some input" # make input to RegisterForm
			reg.return_value = Mock()
			reg.return_value.is_valid = Mock(return_value=False) # make it pass the if part.
			reg.return_value.register_form = Mock(return_value=None)
			with patch('user_auth.views.render_to_response') as render:
				render.return_value = "some value"
				register(request)

				# asserts
				reg.assert_called_with("some input")
				self.assertTrue(not reg.return_value.register_form.called)
				self.assertTrue(render.called)

	def test_unit_register_with_get(self):
		"""
		This test function tests if **register()** is called with get method.
		We need to mock

			1. request
			2. RegisterForm
			3. render_to_response
		"""

		with patch('user_auth.views.RegisterForm') as reg:
			request = MagicMock()
			request.method = "GET"
			reg.return_value = Mock()

			# For testing if we execute correct else statement.
			reg.return_value.is_valid = Mock(return_value=False)
			with patch('user_auth.views.render_to_response') as render:
				render.return_value = True
				register(request)

				# asserts
				self.assertTrue(not reg.return_value.is_valid.called)
				self.assertTrue(render.called)


########################################################
####################logout_user unit tests##############
	def test_unit_logout_user(self):
		"""
		This function tests **logout_user()** function.
		We need to mock

			1. request
			2. render_to_response
			3. logout
		"""

		with patch('user_auth.views.logout') as logout:
			request = MagicMock()
			with patch('user_auth.views.render_to_response') as render:
				logout_user(request)
				logout.assert_called_with(request)
				self.assertTrue(render.called)


########################################################
####################logout_user unit tests##############
	def test_unit_login_user_with_post(self):
		"""
		This function tests **login_user()** with post data.
		We need to mock

			1. request
			2. LogInForm
				- is_valid
				- cleaned_data
			3. authenticate
				- is_active
			4. render_to_response
		"""
		with patch('user_auth.views.LogInForm') as form:
			request = MagicMock()
			request.method = "POST"
			request.POST = "some data"

			form.return_value = Mock()
			form.return_value.is_valid = Mock(return_value=True)
			form.return_value.login_process = Mock()
			with patch('user_auth.views.render_to_response') as render:
				login_user(request)
				form.return_value.login_process.assert_called_with(request)
				form.assert_called_with("some data")
				self.assertTrue(render.called)


########################################################
####################logout_user unit tests##############
	def test_unit_profile_authentication_check(self):
		"""
		For this test, we need to mock

			1. login_required
			2. request
				- user
				- user.is_authenticated
			3. render_to_response
		"""

		with patch('user_auth.views.login_required') as require:
			request = MagicMock()
			request.user.is_authenticated = Mock(return_value=True)
			with patch('user_auth.views.render_to_response') as render:
				profile(request)
				self.assertTrue(render.called)
				request.user.is_authenticated.assert_called_with()


########################################################
####################logout_user unit tests##############
	def test_unit_edit_with_post(self):
		"""
		This function test with post data to **edit()**.
		We need to mock

			1. login_required
			2. request
				- method
			3. EditForm
				- is_valid
				- process
			4. render_to_response
		"""

		with patch('user_auth.views.EditForm') as form:
			request = MagicMock()
			request.method = "POST"
			request.POST = "post data"
			request.FILES = "files"
			request.user = Mock()
			request.user.is_authenticated = Mock(return_value=True)

			form.return_value = Mock()
			form.return_value.is_valid = Mock(return_value=True)
			form.return_value.process = Mock()
			with patch('user_auth.views.login_required') as log:
				with patch('user_auth.views.render_to_response') as render:
					edit(request)
					form.assert_called_with(request.POST, request.FILES)
					self.assertTrue(render.called)
					form.return_value.process.assert_called_with(request.user)

########################################################
####################logout_user unit tests##############
	def test_unit_edit_with_get(self):
		"""
		This tests **edit()** with get method.
		We need to mock 

			1. request
			2. EditForm
			3. render_to_response
		"""

		with patch('user_auth.views.EditForm') as form:
			request = MagicMock()
			request.user = Mock()
			form.return_value = Mock()
			with patch('user_auth.views.render_to_response') as render:
				edit(request)
				self.assertTrue(form.called)
				self.assertTrue(render.called)



#### Integration Tests
###################################################################################
###############Test Register

	def test_register_status_code(self):
		"""
		**test_register_status_code()** checks if a user access to the register page, the status_code
		is 200.
		"""
		# create client.
		response = self.client.get('/user_auth/register/')
		self.assertEqual(response.status_code, 200)



	def test_RegisterForm_get(self):
		"""
		**test_RegisterForm()** checks when request.method to **user_auth.views.register()** is
		GET, the RegisterForm is properly instantiated. 
		"""

		# get method.
		with patch('user_auth.views.RegisterForm') as reg:
			self.client.get('/user_auth/register/')
			# check if RegisterForm is called with post method.
			self.assertTrue(reg.called)

	def test_RegisterForm_post(self):
		"""
		**test_RegisterForm()** checks when request.method to **user_auth.views.register()** is
		POST, the RegisterForm is properly instantiated with appropriate data. This test only 
		checks if the RegisterForm is called with the POST data passed into register().
		"""
		# post method.
		with patch('user_auth.views.RegisterForm') as reg:
			reg.return_value = MagicMock() # only checking if the RegisterForm is called with
									  # proper data.
			reg.return_value.is_valid.return_value = False # this makes form.is_valid() returns False in views.py.
			args = {'user_name':'user1', 'password':'password'}
			self.client.post('/user_auth/register/', args)
			# check if RegisterForm is called with post method.
			reg.assert_called_with(QueryDict('user_name=user1&password=password'))

	@unittest.expectedFailure
	def test_RegisterForm_invalid(self):
		"""
		**test_RegisterForm_validation()** tests if it raise exception when the form is not valid.
		The attributes user_name and password are required. So if the registering user does not pass 
		these two information, the form is not valid.
		"""
		# if the form is not valid, then User.objects.create_user would not be called.
		with patch('user_auth.views.User.objects.create_user') as c_user:
			with patch('user_auth.views.UserInfo.objects.create') as c_userinfo:
				user = c_user.return_value.save = MagicMock()
				userinfo = c_userinfo.return_value.save = MagicMock()
				args = {'password':'password'} # not passing username.
				res = self.client.post('/user_auth/register/', args)

				# user.save() and userinfo.save() must not be called since the form is not valid.
				self.assertTrue(user.save.called or userinfo.save.called)

	@unittest.expectedFailure
	def test_register_notUnique_username(self):
		"""
		**test_register_notUnique_username()** tests if a user trying to register with an username 
		that is already exists in the database. This test should be failed since our website not allow
		two users with same username.
		"""

		username = 'duplicate_username'
		password = 'password'

		# create user.
		user = User.objects.create_user(username=username, password=password)
		args = {'user_name':username, 'password':password}
		self.client.post('/user_auth/register/', args) # this will raise exception.
		User.objects.get(username=username).delete()

###################################################################################
###############Test login_user

	def test_login_status_code(self):
		"""
		**test_login_status_code()** checks if a user access to the login page, the status_code
		is 200.
		"""
		response = self.client.get('/user_auth/login/')
		self.assertEqual(response.status_code, 200)


	def test_LogInForm_get(self):
		"""
		**test_loginForm()** checks if the LogInForm is instantiated when an user access to login page.
		This test should be considered as different test with **test_login_status_code()** since this function just
		checks if the httpresponse returns the status_code 200. 
		"""

		with patch('user_auth.views.LogInForm') as form:
			# access the url.
			# LogInForm is mocked.
			self.client.get('/user_auth/login/')
			form.assert_called_with()

	def test_LogInForm_post(self):
		"""
		**test_LogInForm_post()** tests if the LogINForm is properly instantiated with POST data.
		If the post data looks like {'user_name':'test_user', 'password':'password'}, then the LogInForm
		must be called with the argument **QueryDict('user_name=test_user&password=password')**.
		"""

		args = {'user_name':'test_user', 'password':'password'}
		with patch('user_auth.views.LogInForm') as form:
			# make the function not to log the user in.
			form.return_value.is_valid = MagicMock(return_value=False)
			self.client.post('/user_auth/login/', args)
			form.assert_called_with(QueryDict('user_name=test_user&password=password'))

	@unittest.expectedFailure
	def test_login_user_invalid_username(self):
		"""
		**test_login_user_invalid_username()** tests if an user tries to login with invalid username such as
		non-exist username.
		"""

		args = {'user_name':'user', 'password':'password'}
		if len(User.objects.get(username=args['user_name'])):
			User.objects.get(username=args['user_name']).delete()

		self.client.post('/user_auth/login/', args) # This will throw exception.




###################################################################################
###############Test login_user

	def test_profile_status_code(self):
		"""
		**test_profile_status_code()** checks if a user access to the profile page, the status_code
		is 200.
		"""
		# user must be logged in.
		user = User.objects.create_user(username='test_profile_user', password='password')
		self.client.login(username='test_profile_user', password='password')
		response = self.client.get('/user_auth/profile/')
		User.objects.get(username='test_profile_user').delete()
		self.assertEqual(response.status_code, 200)


	def test_profile_not_logged_in(self):
		"""
		**test_profile_not_logged_in()** tests the status code of http response when the user
		who tries to access the profile page is not logged in. The status code should not be 200.
		"""

		response = self.client.get('/user_auth/profile/')
		self.assertTrue(response.status_code != 200)		



###################################################################################
###############Test login_user

	def test_edit_status_code(self):
		"""
		**test_edit_status_code()** checks if a user access to the edit page, the status_code equals to 200.
		"""
		User.objects.create_user(username='edit_status_code', password='password')
		self.client.login(username='edit_status_code', password='password')
		response = self.client.get('/user_auth/edit/')
		User.objects.get(username='edit_status_code').delete()
		self.assertEqual(response.status_code, 200)

	def test_edit_EditForm_get(self):
		"""
		**test_edit_EditForm_get()** tests if the EditForm is properly instantiated when 
		request.method is GET method. 
		"""
		User.objects.create_user(username='edit_EditForm', password='password')
		self.client.login(username='edit_EditForm', password='password')
		with patch('user_auth.views.EditForm') as form:
			self.client.get('/user_auth/edit/')
			User.objects.get(username='edit_EditForm').delete()
			form.assert_called_with()

	def test_edit_EditForm_post(self):
		"""
		**test_edit_EditForm_post()** tests if the EditForm is properly instantiated with 
		appropriate post data when request.method is POST method. 
		"""
		# create temp user.
		user = User.objects.create_user(username='edit_EditForm', password='password')
		UserInfo.objects.create(user=user)
		# log the user in.
		self.client.login(username='edit_EditForm', password='password')

		# make fake file
		file = SimpleUploadedFile('filename.png', 'image_content')
		dic = MultiValueDict({'picture':file})
		# mock user.save() so that we not really saving the test user.
		with patch('user_auth.views.User.save') as user_save:
			user_save.return_value = None
			self.client.post('/user_auth/edit/', {'first_name':'name', 'last_name':'last_name'} )
			user_save.assert_called_with()
		User.objects.get(username='edit_EditForm').delete()

	# def test_edit_EditForm_file(self):
	# 	"""
	# 	This test the request.FILE in the edit function.
	# 	"""
	# 	# create temp user.
	# 	User.objects.create_user(username='edit_EditForm', password='password')
	# 	# log the user in.
	# 	self.client.login(username='edit_EditForm', password='password')

	# 	# make fake file
	# 	file = SimpleUploadedFile('filename.png', 'image_content')
	# 	# mock user.save() so that we not really saving the test user.
	# 	with patch('user_auth.views.UserInfo.save') as info_save:
	# 		with patch('user_auth.views.EditForm.is_valid') as valid:
	# 			valid.return_value = True
	# 			info_save.return_value = None
	# 			self.client.post('/user_auth/edit/', {'picture':file})
	# 			info_save.assert_called_with()
	# 	User.objects.get(username='edit_EditForm').delete()


	# def test_auth_forms_register_user(self):
	# 	"""
	# 	This function checks if the function *register_user* in **auth_forms.py** was called with
	# 	appropriate data.
	# 	"""

	# 	with patch('Register')
