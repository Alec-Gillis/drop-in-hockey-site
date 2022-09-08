from django.db import models

# Create your models here.
class Player(models.Model):
	name = models.CharField(max_length=35)
	is_checked_in = models.BooleanField(default=False)
	is_goalie = models.BooleanField(default=False)
	is_substitute = models.BooleanField(default=False)

	def __str__(self):
		return self.name