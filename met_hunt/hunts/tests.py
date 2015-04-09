"""
Unit tests for 'hunts' django application

The list of tests are:

"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from hunts.views import getData, assign_vars, render_clue, verify_ID, render_result, render_verify, next_proc, render_congrats, render_clue, render_hunt, TEMP, item_clue, item_id, hunt_title, hunt_start #  *global vars*
from hunts import models

# Create your tests here.
class hunts_test(TestCase):
	def setUp(self):
		self.client = Client()

	def test_hunts_status(self):
		resp = self.client.get('/hunts/') #should be directory of welcom page
		self.assertEqual(resp.status_code, 200)

	def test_getData(self):
#		hunt_ID_mock = mock.Mock()
#		has_mock = mock.Mock(spec=models.Has)
		@patch		
		with patch('hunts.views.getData') as reg:
			self.client.get('/hunts/')#should be directory where hunt is initilized
			reg.called
			if (reg.called):
				
			pass
			#call query
			#use fixtures to fill database and grab from there
			#use count to check that something was grabbed

	def test_assign_vars(self):
		with patch('hunts.views.assign_vars') as reg:
			pass
			#call query
			#check if passed in var matches global vars

	def test_render_clue(self):
		with patch('hunts.views.render_clue') as reg:
			pass
			#assign a val to clue_var
			#self.client.get('path of clue html')
			#reg.called
			#check if clue_var is in content

	def test_verify_ID(self):
		with patch('hunts.views.verify_ID') as reg:
			pass
			#google how to do this one

	def test_render_verify(self):
		with patch('hunts.views.render_verify') as reg:
			pass
			#assign val to ID_var
			#check that next button links to next_proc

	def test_next_proc(self):
		with patch('hunts.views.next_proc') as reg:
			pass
			#call query
			#assign it to temp
			#check if next_proc returns redirect to render_clue
			#empty temp
			#check if next_proc redirect to render_congrats

	def test_congrats(self):
		with patch('hunts.views.render_congrats') as reg:
			pass
			#self.client.get('path')
			#reg.called
