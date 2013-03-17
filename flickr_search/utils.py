def build_flickr_photo_urls(flickr_results=None):
	urls = []
	flickr_url_form_simple = "http://farm{farm}.staticflickr.com/{server}/{id}_{secret}.jpg"
	for result in flickr_results:
		urls.append(flickr_url_form_simple.format(**result.attrib))
	return urls
