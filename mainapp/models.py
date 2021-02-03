from django.db import models
from django.urls import reverse

class Task(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	done = models.BooleanField(default=False)

	class Meta:
		unique_together = ('name', 'date_added')
		ordering = ['date_added']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('task-detail', args=[str(self.id)])
