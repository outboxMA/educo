from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from courses.models import Course
from core.models import Activity
from django.utils import timezone

@receiver(post_save, sender=Course)
def create_activity(sender, instance, created, **kwargs):
    if created:
        Activity.objects.create(title=f"New course \"{instance.title}\" added.", type='course_created', date=timezone.now())

    else:
        Activity.objects.create(title=f"Course \"{instance.title}\" updated.", type='course_updated', date=timezone.now())

@receiver(post_delete, sender=Course)
def delete_activity(sender, instance, **kwargs):
    Activity.objects.create(title=f"Course \"{instance.title}\" deleted.", type='course_deleted', date=timezone.now())