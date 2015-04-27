from django.db import models
from django.contrib.auth.models import User
# Create your models here.

thread_type = (
		('modern', 'Modern Hunt'),
		('ancient', 'Ancient'),
		('general', 'General')
	)

# thread
class Thread(models.Model):
	"""
	This model **Thread** is type of category that is related to the type of questions
	asked by the users. Each thread can have many questions that is related to the 
	type of the thread. 
	"""

	type = models.CharField(max_length=50, choices = thread_type, default = 'general')
	description = models.CharField(max_length=100)
	total_post = models.IntegerField(default=0)

	def __str__(self):
		return self.type


class QuestionAsked(models.Model):
	"""
	This model **QuestionAsked** is related to the questions that a user asked on the website. It 
	has *title*, *description* and the *status* which indicate if the question is answered or not. This model should be
	one-to-many from user to QuestionAsked since each user can have many asked questions.
	"""

	user = models.ForeignKey(User)
	thread = models.ForeignKey(Thread) #Many questions can be belong to a thread.
	title = models.CharField(max_length=50)
	description = models.TextField()
	status = models.BooleanField(default=False)
	when = models.DateTimeField(auto_now_add=True)
	view = models.IntegerField(default=0)

	def __str__(self):
		return "%s's Questions" % (self.user.username)

class Answered(models.Model):
	"""
	Any question can be answered by some other users. **Answered** is model to relate a question 
	is answered by whom and when. Many questions can be aswered by many users.
	"""

	# Each question can be marked as answered by one user.
	questionBy = models.ForeignKey(QuestionAsked) # answer <many> - to - <one> question. A question can have many answers.
	answeredBy = models.ForeignKey(User) # user name.
	when = models.DateField(auto_now_add=True)
	description = models.TextField()
	
	def __str__(self):
		return "The question %s is answered by %s" % (self.questionBy.title, self.answeredBy.username)
