from django.test import TestCase
from mock import MagicMock, Mock, patch
import unittest
from forum import views

# Create your tests here.


class Forum_test(unittest.TestCase):
	"""
	This is forum test.
	"""

	def test_basic(self):
		"""
		This function tests if thread_layout, modern, create function returns
		right templates.
		"""

		with patch('forum.views.render_to_response') as render:
			request = MagicMock()
			render.return_value = "template"
			self.assertEqual("template", views.thread_layout(request))
			self.assertEqual("template", views.modern(request))
			self.assertEqual("template", views.create(request))

	def test_load_data(self):
		"""
		This function tests **load_data()** that is responsible for 
		posts data for the forum.
		"""

		with patch('forum.views.Thread') as thread:
			with patch('forum.views.QuestionAsked') as question:
				with patch('forum.views.JsonResponse') as res:
					request = MagicMock()
					request.method = "GET"
					# thread.objects.get = MagicMock()
					# question.objects.filter.order_by = MagicMock(return_value="something")
					views.load_data(request)
					self.assertTrue(res.called)
					# self.assertTrue(question.objects.order_by.called)
					# self.assertTrue(thread.called)

	@patch('forum.views.render_to_response')
	@patch('forum.views.json.loads')
	@patch('forum.views.User.objects.get')
	@patch('forum.views.Thread.objects.get')
	@patch('forum.views.QuestionAsked.objects.create')
	def test_submit(self, render, loads, user, thread, question):
		"""
		This function tests **submit()**.
		"""
		loads.return_value = "return"
		request = MagicMock()
		request.body = "body of the request"
		views.submit(request)
		self.assertTrue(render.called)

		# with patch('forum.views.render_to_response') as render:
		# 	with patch('forum.views.json.loads') as loads:
		# 		request = MagicMock()
		# 		request.body = "body of the request"
		# 		views.submit(request)
		# 		self.assertTrue(render.called)