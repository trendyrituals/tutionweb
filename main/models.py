from django.db import models

# Create your models here.

class ImgData(models.Model):
	title = models.CharField(max_length=200, blank=False)
	img = models.ImageField(blank=False)

	def __str__(self):
		return self.title
