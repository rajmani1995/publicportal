from django.db import models
from django.contrib.auth.models import User


class Complain(models.Model):
	id=models.AutoField(primary_key=True)
	title= models.CharField(max_length=100)
	type=models.CharField(max_length=10)
	description=models.TextField()
	difficulty=models.IntegerField(default=0)
	userid=models.IntegerField(null=True)
# Create your models here.
class Mapobject(models.Model):
	user = models.OneToOneField(User)
	latitude = models.CharField(max_length = 30)
	longitude = models.CharField(max_length = 30)
