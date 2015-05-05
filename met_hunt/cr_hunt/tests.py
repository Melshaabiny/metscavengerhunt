"""
Unit tests for 'hunts' django application

The list of tests are:

"""
from django.test.client import RequestFactory
from django.test import  Client, TestCase
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from cr_hunt import views 
from cr_hunt import models
from django.core.urlresolvers import reverse
# Create your tests here.
class hunts_test(TestCase):
        def setUp(self):
		views.hunt_id = 111222
		views.i_counter = 0
		pass

	def tearDown(self):
		del views.hunt_id
		del views.i_counter
		pass

	def test_render_main(self):
		"""
			* Will test that correct url is called
		"""
		with patch('cr_hunt.views.render_to_response') as rend:
			request = MagicMock()
			views.render_main(request)
			assert rend.called # Check that rend got called
			rend.assert_called_with("cr_hunt/cr_hunt_main.html") # Check that correct url is called
			self.assertEqual(views.hunt_id, 12349) #check that hunt_id got reassigned correctly
			self.assertEqual (views.i_counter, 0) #check that i_counter is initialized to 0

	def test_render_ats(self):
		"""
			* Will test that correct url is called with csrf token
		"""
		with patch('cr_hunt.views.render_to_response') as rend:
			request = MagicMock()
			views.render_ats(request)
			c_srf = MagicMock()
			assert rend.called # Check that rend got called
			#rend.assert_called_with("cr_hunt/cr_hunt_title_strt.html", c_srf, {}) # check that rend got called with correct url and arguments

	def test_render_aitem(self):
		"""
			* Test that correct checks are performed and that form is generated and passed in as argument
		"""
		with patch('cr_hunt.views.render_to_response') as rend:
			with patch('cr_hunt.views.ItemForm') as form_func:
				request = MagicMock()
				request.method = MagicMock()
				request.method.return_value = "POST"
				form_func.is_valid = MagicMock()
				form_func.is_valid.return_value = True
				views.render_aitem(request)
				assert rend.called

	def test_render_end(self):
		"""
			* Test that rend is called with correct url
		"""
		with patch('cr_hunt.views.render_to_response') as rend:
			request = MagicMock()
			views.render_end(request)
			assert rend.called #check that rend is called
			rend.assert_called_with("cr_hunt/cr_hunt_end.html")

	def test_render_proc_ts(self):
		"""
			* Test that items are grabbed correctly
		"""
		pass




##############**** Model tests

	def test_add_hunt_its(self): #incomplete
		"""
			* Test that correct items are added
		"""
		with patch('cr_hunt.models.cr_Hunts.objects.create') as cr_obj:
			id_hunt = '123'
			title = 'test title'
			start = 'test start'
			cr_obj.Title = MagicMock()
			cr_obj.Title.return_value = None
			cr_obj.Start = MagicMock()
			cr_obj.Start.return_value = None
			#cr_obj.save() = MagicMock()
			cr_obj.save().return_value = None
			models.add_hunt_its(id_hunt,title,start)
			self.assertEqual(cr_obj.Title, title) # Check that correct title is passed through
			self.assertEqual(cr_obj.Start, start) # Check that correct start point is passed through
			assert cr_obj.save().called # Check that data save was called
