from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .queryset import BookQuerySet


class Book(models.Model):
    isbn13 = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    description = models.TextField()
    authors = models.ManyToManyField('catalog.Author')
    publisher = models.ForeignKey('catalog.Publisher')

    objects = BookQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=(self.pk,))

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


def user_for_author(sender, instance, created, **kwargs):
    if created:
        user = User.objects.filter(email=instance.email).first()
        full_name = user.get_full_name()
        Author.objects.filter(pk=instance.pk).update(name=full_name)

post_save.connect(user_for_author, sender=Author)
