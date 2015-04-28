from django.conf.urls import patterns, url
from hunts import views

urlpatterns = patterns('',
    url(r'^welcome/(?P<given_id>[0-9]{3})$', views.render_hunt, name='hunt_welcome'),
    url(r'^clue$', views.render_clue, name='rend_clue'),
    url(r'^verify$', views.render_verify, name='rend_verify'),
    url(r'^hint$', views.render_hint, name='rend_hint'),
    url(r'^result$', views.render_result, name='rend_result'),
    url(r'^correct$', views.render_correct, name='rend_correct'),
    url(r'^next$', views.next_proc, name='next_proc'),
    url(r'^incorrect$', views.render_incorrect, name='rend_incorrect'),
    url(r'^congrats$', views.render_congrats, name='rend_congrats'),

)

