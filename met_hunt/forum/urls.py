from django.conf.urls import patterns, url
#from django.contrib import admin
from forum import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'met_hunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thread/$', views.thread_layout, name='thread_layout'),
    url(r'^thread/modern/$', views.modern, name='modern'),
    url(r'^thread/load_data/$', views.load_data, name='load_data'),
    url(r'^thread/create/$', views.create, name='create'),
    url(r'^thread/submit/$', views.submit, name='submit'),
    url(r'^thread/post/([1-9])+/$', views.post, name='post'),
)
