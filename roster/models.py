from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=35)
	is_checked_in = models.BooleanField(default=False)
	time_checked_in = models.DateTimeField()
	is_goalie = models.BooleanField(default=False)
	is_substitute = models.BooleanField(default=False)

	def __str__(self):
		return "{0} {1}".format(self.name, self.time_checked_in)

class HeaderText(models.Model):
	"""
	Used as the header text so that any site admin can change what the header says
	"""
	text = models.TextField()