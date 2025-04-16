from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def add_points(self, points):
        self.points += points
        self.save()

    def subtract_points(self, points):
        if self.points >= points:
            self.points -= points
            self.save()
            return True
        return False

class Coupon(models.Model):
    code = models.CharField(max_length=100)
    points_required = models.PositiveIntegerField(default=100)
    redeemed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    redeemed_at = models.DateTimeField(null=True, blank=True)

    def redeem(self, user):
        if user.profile.subtract_points(self.points_required):
            self.redeemed_by = user
            self.redeemed_at = timezone.now()
            self.save()
            return True
        return False