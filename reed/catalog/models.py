from django.db import models
from django.core.urlresolvers import reverse


class Book(models.Model):
    isbn13 = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    description = models.TextField()
    authors = models.ManyToManyField('catalog.Author')
    publisher = models.ForeignKey('catalog.Publisher')

    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=(self.pk,))

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
