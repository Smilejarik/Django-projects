from django.db import models


class MovieItem(models.Model):
	title = models.TextField(max_length=50)

	def __str__(self):
		return self.title
