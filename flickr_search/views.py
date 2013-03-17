import itertools
import xml.etree.ElementTree as ET

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render

from flickr_search.models import Search 
from flickr_search.forms import SearchForm

import flickrapi
api_key = '3441e0678422fb595b83945e9c8c8ddd'
flickr = flickrapi.FlickrAPI(api_key, cache=True)


def index(request):
	search_query = None
	flickr_results = None
	try:
		latest_search_list = Search.objects.order_by('photo_date')
	except Search.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search_query_unstripped = form.cleaned_data['search'] #.split()
			if search_query_unstripped:
				search_query = [x.strip().split() for x in search_query_unstripped.split(',')]
				search_query = list(itertools.chain.from_iterable(search_query))
				#TODO: insert call to flickr api with search query.
				flickr_results =  flickr.photos_search(tags=search_query, per_page='10')
				#print "flickr_results: ", type(flickr_results), flickr_results[0]
				if flickr_results:
					pass
			#TODO: Add entry to database
	else:
		form = SearchForm()
	return render(request, 'searches/index.html', 
		{'latest_search_list' : latest_search_list, 
		'form' : form, 
		'search_query' : search_query,
		'flickr_results' : flickr_results,
		})
	
def query(request, keywords=None):
	return HttpResponse("Flickr api query %s" % keywords)
