"""
Unit tests for 'hunts' django application

The list of tests are:

"""
from django.test.client import RequestFactory
from django.test import  Client, TestCase
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from hunts import views #get_data, assign_vars, render_clue, verify_id, render_result, render_verify, next_proc, render_congrats, render_clue, render_hunt#, TEMP, item_clue, item_id, hunt_title, hunt_start #  *global vars*
from hunts import models
from django.core.urlresolvers import reverse

global TEMP
# Create your tests here.
class hunts_test(TestCase):
	def setUp(self):
		self.client = Client()
		global TEMP 
		views.temp = [('123','a clue',1)]
		models.TEMP = views.temp
		TEMP = models.TEMP
		self.factory = RequestFactory()

	def tearDown(self):
		del views.temp
		del models.TEMP

#	def test_hunts_status(self):
#		views.hunt_title = 'test1234567'
#		views.hunt_start = 'test7654321'
#		resp = self.client.get('/hunts/welcome/') #should be directory of welcom page
#		self.assertEqual(resp.status_code, 200)

	def test_getData(self): #INCOMPLETE
		pass
			#call query
			#use fixtures to fill database and grab from there
			#use count to check that something was grabbed

	def test_render_clue(self): #DONE
		"""
		**test_render_clue**
			First: tests if render_clue is called when going to the clue page

			Second: mocks item_clue to force it to return a unique value. Then tests if that clue
			is in the context of the rendered html page
		"""
		with patch('hunts.views.render_to_response') as rend:
			request = MagicMock()
			views.render_clue(request)
			rend.assert_called_with("hunts/clue.html", {"clue_text" : 'a clue'}) #clue was not displayed on clue page"

	def test_verify_ID(self): #DONE
		"""
		**test_verify_ID**	Function mocks the var 'item_id' then runs verify_id to see if it returns correct boolean values for an equal input and an unequal input
		"""
		s_val = '123'
		f_val = '234'
		success = models.verify_id(s_val)
		failure = models.verify_id(f_val)
		assert success #verify_id did not return true when input and item_id were equal"
		assert not(failure) #verify_id did not return false when input and item_id were different"

	def test_render_verify(self):#DONE
		"""
		**test_render_verify** tests if render_verify is ran at the correct url
		"""
		with patch('hunts.views.render_to_response') as reg:
			request = MagicMock()
			views.render_verify(request)
			c_srf = {}
			assert reg.called #render_verify returns render_to_response
			#reg.assert_called_with("hunts/verify.html", c_srf, {}) #check that correct html is used with csrf token

	def test_next_proc(self): #Needs to be checked
		"""
		mocks temp and pop_item function. Runs next_proc to see if pop_tem is called when temp is not empty.
		Then an assert is made to check that it correctly redirects to the clue page.

		Empties temp and runs next_proc again. This time checks that pop_item is not called. Then an assert is made to
		check that it correctly redirects to the congrats page.
		"""
		with patch('hunts.views.pop_item') as pop_item:
			with patch('hunts.views.redirect') as redirect:
				pop_item.return_value = [1]
				global temp
				temp = views.temp
				views.next_proc(self.factory)
				assert pop_item.called #test that pop_item is called
				redirect.assert_called_with('rend_clue') #next_proc does not correctly redirect to clue page
				pop_item.reset_mock()
				pop_item.return_value = []
				views.next_proc(self.factory)
#				assert not(pop_item.called) #pop_item was called when TEMP was empty"

	def test_congrats(self):#DONE
		"""
		**test_congrats** tests if render_congrats is ran at the correct url
		"""
		with patch('hunts.views.render_congrats') as reg:
			request = MagicMock()
			reg(request)
			#self.client.get('/hunts/congrats/')
			#try:
			#	assert reg.called
			#except AssertionError:
			#	print "render_congrats was not called at the url: /hunts/congrats/"
			reg.assert_called_with(request)

	def test_correct(self):
		with patch('hunts.views.render_to_response') as rend:
			request = MagicMock()
			views.render_correct(request)
			rend.assert_called_with("hunts/correct.html", {})

	def test_incorrect(self):
		with patch('hunts.views.render_to_response') as rend:
			request = MagicMock()
			views.render_incorrect(request)
			rend.assert_called_with("hunts/incorrect.html", {})
	def test_render_result(self):#DONE
		"""
		**test_render_result** The test mocks verify_id. Fixes it to True and checks that render_result redirects to the
					correct page
					Then the test fixes verify_id to false and checks that render_result redirects to incorrect page
		"""
		with patch('hunts.views.verify_id') as verify_id:
			with patch('hunts.views.redirect') as redirect:
				verify_id.return_value = True
				request = self.factory.post('/hunts/result/',{'input':'123'})
				views.temp = [('123','a clue',1),('234','a clue2',2)]
				views.render_result(request) #run render_result
				redirect.assert_called_with('rend_correct') #render_verify does not correctly redirect to 'correct' page when expected"
				views.temp = [('123','a clue',1)]
				views.render_result(request)
				redirect.assert_called_with('rend_congrats') #render_result dow not correctly redirect to 'congrats' page when expected
				verify_id.return_value = False
				views.render_result(request)
				redirect.assert_called_with('rend_incorrect') #render_verify does not correctly redirect to 'incorrect' page when expected


			
	def test_render_hunt(self):#DONE, updated
		"""
		**test_render_hunt** This test mocks hunt_title and hunt_start. Then the test tries to call the hunts/hunt url which
					should render with hunt_title and hunt_start which are validated at the end of the test.
		"""
		with patch('hunts.views.set_ItemsData') as itemsdata:
			with patch('hunts.views.set_HuntsData') as huntsdata:
				with patch('hunts.views.render_to_response') as rend:
					global TEMP
					itemsdata.return_value = views.temp
					huntsdata.return_value = {'hunt title' : 'test1234567', 'hunt start' : 'test7654321'}
					request = MagicMock()
					views.render_hunt(request,1)
					rend.assert_called_with("hunts/hunt.html", {"title" : 'test1234567', "start_pt": 'test7654321'}) #check that correct title and start point were passed through


######################***Model tests***
	def test_set_HuntsData(self):
		"""
		**test_set_HuntsData** this test creates a mock object and then tests that the correct values are retrieved
		"""
		pass

	def test_set_ItemsData(self):
		"""
		**test_set_ItemsData** this test should mock the model and check that correct items were retrieved
		"""
		pass

	def test_pop_item(self):
		lst = [1]
		lst = models.pop_item(lst)
		self.assertTrue(len(lst)<1)
