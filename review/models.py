from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from place.models import Place

class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(6)]
   
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reviews')
    
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    comment = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.place.name} - {self.rating}'
