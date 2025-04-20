from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    google_maps_link = models.URLField()
    description = models.TextField()

    photo_main = models.ImageField(upload_to='places/')
    photo_1 = models.ImageField(upload_to='places/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='places/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='places/', blank=True, null=True)

    def __str__(self):
        return self.name
