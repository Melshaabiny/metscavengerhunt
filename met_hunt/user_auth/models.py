"""
This user_auth.models defined several user information.

    1. **UserInfo** defines those neccessary user information such as
        the date when each user registered, picture, expert_level and area of expertises.
    2. **FriendList** defines the list of friend for each user. Each user can have many friends.

"""
from django.db import models
from django.contrib.auth.models import User
from hunts.models import HuntProg, Hunts

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

    :user: This is one-to-one relationship from the django User class to UserInfor.
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
        uhunt_title = user_hunts[user_hunt].hunt.Title
        prog_val = user_hunts[user_hunt].cur_item_num
        #under assumption that all hunts have 10 items
        prog_val = (prog_val / 10) * 100
        prog_str = str(prog_val) + ' %'
        lst_hunts = lst_hunts + ((uhunt_title, prog_str),)
    return list(lst_hunts)

def get_createdhunts(unam):
    """
    Grab hunts that were created by a user
    """
    user_hunts = Hunts.objects.filter(user = uname)
    lst_hunts = []
    for user_hunt in user_hunts:
        uhunt_title = user_hunts[user_hunt].Title
        lst_hunts.append(uhunt_title)
    return lst_hunts
