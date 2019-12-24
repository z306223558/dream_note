from django.db.models.signals import post_save
from django.dispatch import receiver

from book.models import Book


@receiver(post_save, sender=Book)
def book_save_handler(sender, instance, **kwargs):
    created = kwargs.get('created', False)
    if not created:
        return
