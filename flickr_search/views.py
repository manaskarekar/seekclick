from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from django.shortcuts import render

from flickr_search.models import Search 
from flickr_search.forms import SearchForm

def index(request):
	search_query = None
	try:
		latest_search_list = Search.objects.order_by('photo_date')
	except Search.DoesNotExist:
		raise Http404
	
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search_query = form.cleaned_data['search'] #.split()
			#TODO: insert call to flickr api with search query.
			#TODO: Add entry to database
			
			#return HttpResponseRedirect('/results/%s' % search_query)
			return HttpResponseRedirect('/results/')
	else:
		form = SearchForm()
	return render(request, 'searches/index.html', {'latest_search_list' : latest_search_list, 'form' : form, 'search_query' : search_query})
	
def results(request, keywords=None):
	return HttpResponse("Flickr query results photos for following keywords: %s" % request.POST['search'])

def query(request, keywords=None):
	return HttpResponse("Flickr api query %s" % keywords)
