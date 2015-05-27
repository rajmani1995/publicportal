from django.db import models
from django.contrib.auth.models import User
from constants import TYPE

class Complaint(models.Model):
	id=models.AutoField(primary_key=True)
	title= models.CharField(max_length=100)
	type=models.CharField(max_length=10)
	description=models.TextField()
	difficulty=models.IntegerField(default=0)
	userid=models.IntegerField(null=True)
	location = models.CharField(max_length = 100)
	latitude = models.CharField(max_length = 30)
	longitude = models.CharField(max_length = 30)
	approved = models.BooleanField(default=True)
	# rating = models.FloatField()
	image = models.ImageField(upload_to='complaint_images',blank=True)
	def __unicode__(self):
		return self.title
class Mapobject(models.Model):
	user = models.OneToOneField(User)
	location = models.CharField(max_length = 100)
	latitude = models.CharField(max_length = 30)
	longitude = models.CharField(max_length = 30)