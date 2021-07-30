from django.db import models

# Create your models here.


class Playlist(models.Model):
	def __str__(self):
		return self.Course_name + "-" + self.Year
		
	Course_name = models.CharField(max_length=100)
	Year = models.CharField(max_length=20)
	Link = models.CharField(max_length=2000)

