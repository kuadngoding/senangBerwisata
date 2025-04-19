from django.db import models
from senangBerwisata import settings

# Create your models here.

class WisataTematik(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='wisata_tematik/')
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    dibuat_oleh = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul
    