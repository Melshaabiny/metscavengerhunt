from django.conf.urls import patterns, url
from home import views


urlpatterns = patterns('',
        url(r'^$', views.main, name='main'),
        url(r'^wiki/$', views.wiki, name='wiki'),
)
