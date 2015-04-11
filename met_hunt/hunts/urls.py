from django.conf.urls import patterns, include, url
from django.contrib import admin

from hunts import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'met_hunt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 
	url(r'^hunts/welcome$',	views.render_hunt, 		name='hunt'),
	url(r'^hunts/clue$', 	views.render_clue, 		name='rend_clue'),
    url(r'^hunts/verify$', 	views.render_verify, 	name='verify_clue'),
	url(r'^hunts/result$', 	views.render_result, 	name='verify_result'),
	url(r'^hunts/congrats$',views.render_congrats, 	name='verify_result'),

)

