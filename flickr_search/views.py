from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. I've been waiting for a chance to see your face.")

def results(request, keywords=None):
	return HttpResponse("Flickr query photos for following keywords: %s" % keywords.split())

def query(request, keywords=None):
	return HttpResponse("<Flickr query>")

def search_action(request, keywords=None):
	return HttpResponse("search action")
