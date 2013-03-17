from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(required=False)
	
	def query_flickr_api():
		pass
