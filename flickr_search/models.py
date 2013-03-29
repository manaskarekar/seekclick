import datetime
from django.db import models
from django.utils import timezone

class Search(models.Model):
	location = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	photo_date = models.DateTimeField('date taken')
	results = models.ManyToManyField('Photo')

	def __unicode__(self):
		return self.location

	def taken_recently(self):
		return self.photo_date >= timezone.now() - datetime.timedelta(days=7)
		
class Photo(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(max_length=200)
	author = models.CharField(max_length=200)
	# geolocation = 
	# interestingness = 
	# 

	searches = models.ManyToManyField('Search')

