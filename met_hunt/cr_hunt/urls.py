from django.conf.urls import patterns, include, url
from django.contrib import admin

from cr_hunt import views

urlpatterns = patterns('',
	url(r'^welcome$', views.render_main , name='cr_main'),
	url(r'^ats$', views.render_ats, name='cr_ats'),
	url(r'^proc_ts$', views.render_proc_ts, name = 'cr_proc_ts'),
    	url(r'^aitem$', views.render_aitem, name='cr_aitem'),
        url(r'^proc_it$', views.render_proc_it, name = 'cr_proc_it'),
	url(r'^end$', views.render_end, name = 'cr_end'),
)
