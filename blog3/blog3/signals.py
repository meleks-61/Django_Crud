from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Post,Category
from .utils import get_random_code#utils kendi yazdıgımız script

@receiver(pre_save,sender=Post)
def pre_save_create_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug=slugify(
            instance.title+""+get_random_code()
        )
@receiver(pre_save,sender=Category)
def pre_save_create_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug=slugify(
            instance.name+""+get_random_code()
        )