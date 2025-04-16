from django.db.models.signals import post_save
from django.dispatch import receiver
from review.models import Review

@receiver(post_save, sender=Review)
def add_points_on_review(sender, instance, created, **kwargs):
    if created:
        user_profile = instance.user.profile
        user_profile.add_points(5)
