"""
Unit tests for 'hunts' django application

The list of tests are:

"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from user_auth.views import login, logout_user, register

# Create your tests here.
class hunts_test(TestCase):
	def setUp(self):
		self.client = Client()

	def test_hunts_status(self):
		resp = self.client.get('/hunts/') #should be directory of welcom page
		self.assertEqual(resp.status_code, 200)

	
