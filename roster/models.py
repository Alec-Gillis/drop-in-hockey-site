from django.db import models
from django.utils import timezone

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=35)
	is_checked_in = models.BooleanField(default=False)
	time_checked_in = models.DateTimeField(default=timezone.now())
	is_goalie = models.BooleanField(default=False)
	is_substitute = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class HeaderText(models.Model):
	"""
	Used as the header text so that any site admin can change what the header says
	"""
	text = models.TextField()