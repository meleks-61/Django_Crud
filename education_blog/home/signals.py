from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import Teacher,Branch
from .utils import get_random_code

@receiver(pre_save,sender=Teacher)
def pre_save_create_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug=slugify(
            instance.name+""+get_random_code()
        )

@receiver(pre_save,sender=Branch)
def pre_save_create_slug(sender,instance,**kwargs):
    if not instance.slug:
        instance.slug=slugify(
            instance.title+""+get_random_code()
        )