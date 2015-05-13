"""
This user_auth.models defined several user information.

    1. **UserInfo** defines those neccessary user information such as
        the date when each user registered, picture, expert_level and area of expertises.
    2. **FriendList** defines the list of friend for each user. Each user can have many friends.

"""
from django.db import models
from django.contrib.auth.models import User
from hunts.models import HuntProg, Hunts
from cr_hunt.models import cr_Hunts

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

    Here are the attributes of the model.

    :user: This is one-to-one relationship from the django User class to UserInfo.
    """


    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='user_auth/user_pic/', blank=True)

    # choices, (c1, c2), c1 is actual value, c2 is label.
    expert_level = models.CharField(max_length=15, choices=level, default='beginner', blank=True)
    area_of_expertise = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s's UserInfo" % (self.user.username)

class FriendList(models.Model):
    """
    Model for friendlist for each user.
    """
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s's Friend" % (self.user.username)

def get_huntprog(uname):
    """
    Grab progress of hunts for a user
    """
    user_hunts = HuntProg.objects.filter(user = uname)
    lst_hunts = ()
    for user_hunt in user_hunts:
        uhunt_title = user_hunt.hunt.Title
        prog_val = float(user_hunt.cur_item_num)
        #under assumption that all hunts have 10 items
        prog_val = (prog_val / 10) * 100
        prog_str = str(prog_val) + ' %'
        lst_hunts = lst_hunts + ((uhunt_title, prog_str),)
    return list(lst_hunts)

def get_createdhunts(uname):
    """
    Grab hunts that were created by a user
    """
    user_hunts = cr_Hunts.objects.filter(CreatedBy = uname)
    #should be Hunts.objects.filter(user = uname)
    lst_hunts = ()
    for user_hunt in user_hunts:
        uhunt_title = str(user_hunt.Title)
        lst_hunts = lst_hunts + ((uhunt_title),)
    return list(lst_hunts)

def get_expertise_lvl_rank(uname):
    """
    Get expertise lvl and calculate score
    input: username
    output: total score
    """
    user_hunt_scores = HuntProg.objects.filter(user = uname)
    t_score = 0
    for score in user_hunt_scores:
        prog_val = float(score.cur_item_num)
        #under assumption that all hunts have 10 items and each hunt is worth 50 points
        prog_val = (prog_val / 10)
        prog_val = prog_val * 50
        t_score = t_score + prog_val
    return t_score
