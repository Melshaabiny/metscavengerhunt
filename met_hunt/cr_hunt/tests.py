"""
Unit tests for 'hunts' django application

The list of tests are:

"""
from django.test.client import RequestFactory
from django.test import  Client, TestCase
from django.contrib.auth.models import User
from mock import MagicMock, Mock, patch
from cr_hunts import views 
from cr_hunts import models
from django.core.urlresolvers import reverse
# Create your tests here.
class hunts_test(TestCase):
        def setUp(self):

