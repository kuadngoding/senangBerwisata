from django.db import models
from django.conf import settings
from place.models import Place

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'place')  

    def __str__(self):
        return f"{self.user.username} - {self.place.name}"
