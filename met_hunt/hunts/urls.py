from django.conf.urls import patterns, include, url
from django.contrib import admin

from hunts import views

urlpatterns = patterns('',
 
	url(r'^hunts/welcome$',		views.render_hunt, 		name='hunt_welcome'),
	url(r'^hunts/clue$', 		views.render_clue, 		name='rend_clue'),
    url(r'^hunts/verify$', 		views.render_verify, 	name='rend_verify'),
	url(r'^hunts/result$', 		views.render_result, 	name='rend_result'),
	url(r'^hunts/correct$', 	views.render_correct, 	name='rend_correct'),
	url(r'^hunts/incorrect$', 	views.render_incorrect, name='rend_incorrect'),
	url(r'^hunts/congrats$',	views.render_congrats, 	name='rend_congrats'),

)

