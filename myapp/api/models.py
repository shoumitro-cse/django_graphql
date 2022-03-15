from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()
    metadata = models.JSONField(default=dict, blank=True, help_text='Metadata of the person.')

    def __str__(self):
        return self.title
