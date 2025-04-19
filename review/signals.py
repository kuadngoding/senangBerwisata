from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review

@receiver(post_save, sender=Review)
def update_user_points(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.points += 50
        user.save(update_fields=['points'])