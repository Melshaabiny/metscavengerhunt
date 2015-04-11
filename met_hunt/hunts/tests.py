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

	def tearDown(self):
		pass

	def test_hunts_status(self):
		resp = self.client.get('/hunts/') #should be directory of welcom page
		self.assertEqual(resp.status_code, 200)

	def test_getData(self): #INCOMPLETE
#		hunt_ID_mock = mock.Mock()
#		has_mock = mock.Mock(spec=models.Has)
		with patch('hunts.views.getData') as reg:
			self.client.get('/hunts/')#should be directory where hunt is initilized
			reg.called
			#call query
			#use fixtures to fill database and grab from there
			#use count to check that something was grabbed

	def test_assign_vars(self): #DONE
	"""
	**test_assign_vars**	Mocks item_id item_clue and the TEMP dictionary. Then calls assign_vars. The uses assert calls to check that the correct values were assigned to item_id and item_clue
	"""
		with patch('hunts.views.item_id') as item_id:
			with patch('hunts.views.item_clue') as item_clue:
				with patch.dict(TEMP, {'123':'a clue'}, clear=True):
					assign_vars()
					assert item_id == '123'
					except AssertionError:
						print "item_id was not correctly assigned in assign_vars"
					assert item_clue == 'a clue'
					except AssertionError:
						print "item_clue was not correctly assigned in assign_vars"


	def test_render_clue(self): #DONE
	"""
	**test_render_clue**
		First: tests if render_clue is called when going to the clue page

		Second: mocks item_clue to force it to return a unique value. Then tests if that clue
			is in the context of the rendered html page
	"""
		with patch('hunts.views.render_clue') as reg:
			self.client.get('/hunts/clue/')
			assert reg.called
			except AssertionError:
				print "render_clue was not called"
		with patch('hunts.views.item_clue') as item_clue:
			item_clue.return_value = 'test12345678'
			response = self.client.get('/hunts/clue/')
			assert 'test12345678' in response.content
			except AssertionError:
				print "clue was not displayed on clue page"

	def test_verify_ID(self): #DONE
	"""
	**test_verify_ID**	Function mocks the var 'item_id' then runs verify_id to see if it returns correct boolean values for an equal input and an unequal input
	"""
		with patch('hunts.views.item_id') as item_id:
			item_id.return_value = '123'
			s_val = '123'
			f_val = '234'
			success = verify_id(s_val)
			failure = verify_id(f_val)
			assert success
			except AssertionError:
				print "verify_id did not return true when input and item_id were equal"
			assert not(failure)
			except AssertionError:
				print "verify_id did not return false when input and item_id were different"

	def test_render_verify(self):#INCOMPLETE - test if links are correct
	"""
	**test_render_verify** tests if render_verify is ran at the correct url
	"""
		with patch('hunts.views.render_verify') as reg:
			self.client.get('/hunts/verify/')
			assert reg.called
			except AssertionError:
				print "render_verify was not called at the url: /hunts/verify/"

		
			#assign val to ID_var
			#check that next button links to next_proc

	def test_next_proc(self): #Needs to be checked
	"""
		mocks TEMP and assign_vars function. Runs next_proc to see if assign_vars is called when TEMP is not empty.
		Then an assert is made to check that it correctly redirects to the clue page.

		Empties TEMP and runs next_proc again. This time checks that assign_vars is not called. Then an assert is made to
		check that it correctly redirects to the congrats page.
	"""
		with patch.dict(TEMP, {'123':'a clue'}, clear=True):
			with patch('hunts.views.assign_vars') as reg:
				reg.return_value = None
				next_proc()
				reg.called #test that assign_vars is called when TEMP is not empty
				try:
					self.assertRedirects(next_proc(),'/hunts/clue/') #should redirect to clue
				except Exception as e:
					print "next_proc does not correctly redirect to clue page when expected"
				TEMP = {}
				next_proc()
				assert not(reg.called)
				except AssertionError:
					print "assign_vars was called when TEMP was empty"
				try:
					self.assertRedirects(next_proc(),'/hunts/congrats/') #should redirect to congrats
                                except Exception as e:
                                        print "next_proc does not correctly redirect to congrats page when expected"

	def test_congrats(self):#DONE
	"""
	**test_congrats** tests if render_congrats is ran the correct url
	"""
		with patch('hunts.views.render_congrats') as reg:
			self.client.get('/hunts/congrats/')
			assert reg.called
			except AssertionError:
				print "render_congrats was not called at the url: /hunts/congrats/"

	def test_render_result(self):#INCOMPLETE
	""""
	**test_render_result**
	"""
		with patch('hunts.views.verify_id') as verify_id:
			verify_id.return_value = True
			
	def test_render_hunt(self):#incomplete
