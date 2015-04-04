"""
Unit test for **user_auth** djanfo application.
The list of tests are : 
	1. If anyone who try to access the url "/user_auth/register/" 
	successfully access to the page.
	2. If anyone who try to access the url "/user_auth/login/" 
	successfully access to the page.
	3. The register view in user_auth.views correctly 
	register the visitor.
	
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.
class user_authTest(TestCase):

	def setUp(self):
		self.client = Client()

	def tearDown(self):
		User.objects.all().delete() # clean up the user database.

	def test_register_status_code(self):
		# create client.
		client = Client()
		response = client.get('/user_auth/register/')
		self.assertEqual(response.status_code, 200)

	def test_login_status_code(self):
		client = Client()
		response = client.get('/user_auth/login/')
		self.assertEqual(response.status_code, 200)

	def test_registering_check(self):
		user_name = 'test1_user'
		response = self.client.post('/user_auth/register/', {'user_name':user_name, 'password':'test1_user'})

		# It seems that after passing user info using client.post,
		# the registering does not effected right away.
		# get user name we just registered.
		u_name = User.objects.get(username = user_name)
		self.assertEqual(user_name, u_name.username)