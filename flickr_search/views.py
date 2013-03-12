from django.http import HttpResponse
from flickr_search.models import Search 
def index(request):
	latest_search_list = Search.objects.order_by('photo_date')
	output = ', '.join([s.keywords for s in latest_search_list])
	return HttpResponse(output)

def results(request, keywords=None):
	return HttpResponse("Flickr query results photos for following keywords: %s" % keywords.split())

def query(request, keywords=None):
	return HttpResponse("<Flickr api query>")

def search(request, keywords=None):
	return HttpResponse("search for '%s'" % keywords)
