# from django.db import models
from django.contrib.auth.models import User
from hunts.models import HuntProg
from user_auth.models import get_expertise_lvl_rank
# # Create your models here.

def get_leaderboard():
    Users_reg = User.objects.all()
    lst = ()
    for user_reg in Users_reg:
        uname = user_reg.username
        score = get_expertise_lvl_rank(uname)
        uname_str = str(uname)
        lst = lst + ((uname_str, score),)
    return list(lst)
    
