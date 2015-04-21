from django.conf.urls import patterns, include, url
from django.contrib import admin
from forum import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'met_hunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^thread/$', views.thread_main, name='thread_main'),
	url(r'^thread/modern_thread/$', views.modern_thread, name='modern_thread'),
	url(r'^thread/modern_thread/load_data/$', views.load_data, name='load_data'),
)
