from django.contrib.auth.models import User
from django.db.models.signals import post_save

from .models import Author


def user_for_author(sender, instance, created, **kwargs):
    if created:
        user = User.objects.filter(email=instance.email).first()
        full_name = user.get_full_name()
        Author.objects.filter(pk=instance.pk).update(name=full_name)

post_save.connect(user_for_author, sender=Author)
