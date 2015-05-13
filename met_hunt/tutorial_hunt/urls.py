from django.conf.urls import patterns, include, url
from django.contrib import admin
from tutorial_hunt import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'met_hunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
        url(r'^verify/$', views.verf_clue, name='verify_clue'),
	url(r'^$',views.rend_welcome,name='rend_welcome'),
	url(r'^clue/$', views.rend_clue, name='rend_clue'),
)

