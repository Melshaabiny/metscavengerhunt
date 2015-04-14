from django.contrib import admin

# Register your models here.
from user_auth.models import UserInfo, FriendList, QuestionAsked, Answered

admin.site.register(UserInfo)
admin.site.register(FriendList)
admin.site.register(QuestionAsked)
admin.site.register(Answered)