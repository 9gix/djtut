from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    isbn13 = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=(self.pk,))
