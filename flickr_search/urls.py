from django.conf.urls import patterns, url
from flickr_search import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^search/(?P<keywords>\w+)/$', views.search, name='search'),
		url(r'^query/(?P<keywords>\w+)/$', views.query, name='query'),
		url(r'^results/(?P<keywords>\w+)/$', views.results, name='results'),
		)
