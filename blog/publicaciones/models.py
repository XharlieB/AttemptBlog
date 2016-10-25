from django.db import models

# Create your models here.


class Post(models.Model):

	postName = models.CharField(max_length=80)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey('auth.User')

	def __str__(self):
		return self.postName
