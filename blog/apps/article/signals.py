import hashlib
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from apps.article.models import Article


@receiver(pre_save, sender=Article)
def add_slug_to_question(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = hashlib.md5((slug + "-" + random_string).encode('utf-8')).hexdigest()
