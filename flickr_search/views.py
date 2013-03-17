import itertools
import xml.etree.ElementTree as ET

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render

from flickr_search.models import Search 
from flickr_search.forms import SearchForm

from utils import build_flickr_photo_urls

import flickrapi
api_key = '3441e0678422fb595b83945e9c8c8ddd'
flickr = flickrapi.FlickrAPI(api_key, cache=True)


def index(request):
	search_query = None
	flickr_results = None
	flickr_photo_urls = None
	keywords = None
	try:
		latest_search_list = Search.objects.order_by('photo_date')
	except Search.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search_query_unstripped = form.cleaned_data['search'] #.split()
			if search_query_unstripped:
				keywords = [x.strip().split() for x in search_query_unstripped.split(',')]
				keywords = list(itertools.chain.from_iterable(keywords))
				search_query = ",".join(keywords)
				flickr_results =  flickr.photos_search(tags=search_query, per_page='10', sort='interestingness-desc')
				if flickr_results:
					flickr_result = flickr_results.find('photos')
					flickr_photo_urls = build_flickr_photo_urls(flickr_result)
					#print flickr_result, flickr_photo_urls
					#for photo in flickr_result:
					#	print photo.tag, photo.attrib, "<"
			#TODO: Add entry to database
	else:
		form = SearchForm()
	return render(request, 'searches/index.html', 
		{'latest_search_list' : latest_search_list, 
		'form' : form, 
		'keywords' : keywords,
		'flickr_photo_urls' : flickr_photo_urls,
		})
	
def query(request, keywords=None):
	return HttpResponse("Flickr api query %s" % keywords)
