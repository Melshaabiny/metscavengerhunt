from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'met_hunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('home.urls')),
	url(r'^user_auth/', include('user_auth.urls')),
	url(r'^tutorial/',include('tutorial_hunt.urls')),
	url(r'^hunts/',include('hunts.urls')),
)
