from django.db import models
from django.utils import timezone

# define our model (object)
class Post(models.Model):
	# define properties and each field within a listed property

	#ForeignKey links to another model
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	# CharField is how to define text within a limited number of characters
	title = models.CharField(max_length=200)
	# TextField is for long text without a limit
	text = models.TextField()
	# Date and time to be saved
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title