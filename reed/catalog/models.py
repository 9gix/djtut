from django.db import models


class Book(models.Model):
    isbn13 = models.CharField(max_length=13)
    title = models.CharField(max_length=200)
    description = models.TextField()
