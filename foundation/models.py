from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mapobject(models.Model):
	user = models.OneToOneField(User)
	latitude = models.CharField(max_length = 30)
	longitude = models.CharField(max_length = 30)