from django.contrib import admin
# Register your models here.
from user_auth.models import UserInfo, FriendList

admin.site.register(UserInfo)
admin.site.register(FriendList)