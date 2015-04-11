from django.conf.urls import patterns, url
from user_auth import views


urlpatterns = patterns('',
		url(r'^login/$', views.login_user, name='login'),
		url(r'^register/$', views.register, name='register'),
		url(r'^logout/$', views.logout_user, name='logout'),
		url(r'^profile/$', views.profile, name='profile'),
		url(r'^edit/$', views.edit, name='edit'),

)