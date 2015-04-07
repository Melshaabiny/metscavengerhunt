"""
This user_auth.models defined several user information.

	1. **UserInfo** defines those neccessary user information such as the date when each user registered,
	picture, expert_level and area of expertises.
	
	2. **FriendList** defines the list of friend for each user. Each user can have many friends.
"""
from django.db import models
from django.contrib.auth.models import User

level = (
	('expert', 'Expert'),
	('itermmediate', 'Intermmediate'),
	('beginner', 'Beginner')
	)

# Create your models here.
class UserInfo(models.Model):
	"""
	**UserInfo** model defines extra user information such as picture, expert level and areas, and 
	their description. 
	"""


	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='user_auth/user_pic/', blank=True)

	# choices, (c1, c2), c1 is actual value, c2 is label.
	expert_level = models.CharField(max_length=15, choices=level, default='beginner', blank=True)
	area_of_expertise = models.CharField(max_length=30, blank=True)
	description = models.TextField(blank=True)
	
	def __str__(self):
		return "%s's UserInfo" % (self.user.username)

class QuestionAsked(models.Model):
	"""
	This model **QuestionAsked** is related to the questions that a user asked on the website. It 
	has *title*, *description* and the *status* which indicate if the question is answered or not. This model should be
	one-to-many from user to QuestionAsked since each user can have many asked questions.
	"""

	user = models.ForeignKey(User)
	title = models.CharField(max_length=50)
	description = models.TextField()
	status = models.BooleanField(default=False)
	when = models.DateField(auto_now_add=True)

	def __str__(self):
		return "%s's Questions" % (self.user.username)

class Answered(models.Model):
	"""
	Any question can be answered by some other users. **Answered** is model to relate a question 
	is answered by whom and when. Many questions can be aswered by many users.
	"""

	# Each question can be marked as answered by one user.
	questionBy = models.ForeignKey(QuestionAsked)
	answeredBy = models.OneToOneField(User) # user name.
	when = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return "Answered by %s" % (self.answeredBy.username)

class FriendList(models.Model):
	user = models.ForeignKey(User)

	def __str__(self):
		return "%s's Friend" % (self.user.username)