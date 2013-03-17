from django import forms

class SearchForm(forms.Form):
	search = forms.CharField()
	
	def query_flickr_api():
		pass
