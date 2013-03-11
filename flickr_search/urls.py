from django.conf.urls import patterns, url
from flickr_search import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^(?P<keywords>\[A-Za-z0-9_]+)/results/', views.results, name='results'),
		url(r'^(?P<keywords>\d+)/query/^$', views.query, name='query'),
		url(r'^(?P<keywords>\d+)/search_action/^$', views.search_action, name='search_action'),
		#url(r'^(?P<keywords>\d+)/search_action/^$', views.search_action, name='search_action'),
		)
