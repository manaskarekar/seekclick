import datetime
from django.db import models
from django.utils import timezone

class Search(models.Model):
	location = models.CharField(max_length=200)
	keywords = models.CharField(max_length=200)
	photo_date = models.DateTimeField('date taken')

	def __unicode__(self):
		return self.location

	def taken_recently(self):
		return self.photo_date >= timezone.now() - datetime.timedelta(days=7)
