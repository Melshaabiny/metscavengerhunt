from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'met_hunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^thread/$', views.thread_main, name='thread_main'),
)
