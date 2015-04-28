from random import randrange
from forum.models import QuestionAsked, Thread
from django.contrib.auth.models import User

sample = "ABCDEFGHIJKLMNabcdefgzxnmlkpoi123456789"
thread = Thread.objects.get(type='modern')
try:
	user = User.objects.get(username='user4')
except:
	user = User.objects.create_user(username='user4', password='user')

def make_title(size, sample):
	title = ""
	for i in range(size):
		title += sample[randrange(0,len(sample))]
	return title

def make_description(size, sample):
	description = ""
	for i in range(size):
		description += sample[randrange(0, len(sample))]

	return description

for i in range(15):
	title = make_title(randrange(8,20), sample)
	description = make_description(randrange(15,30), sample)
	post = QuestionAsked(title = title, description = description, user = user, thread = thread)
	post.save()