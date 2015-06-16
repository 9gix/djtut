from django.db import models
from django.db.models import Q


class BookQuerySet(models.QuerySet):
    def intro_book(self):
        return self.filter(title__icontains='101')

    def python_book(self):
        return self.filter(Q(title__icontains='django')|Q(title__icontains='python'))
