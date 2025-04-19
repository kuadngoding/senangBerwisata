from django.db import models
from django.conf import settings
import random
import string

class Coupon(models.Model):
    BRAND_CHOICES = [
        ('Hotel',       'Diskon Hotel 30%'),
        ('Travel',      'Voucher Travel Rp100.000'),
        ('Photobooth',  'Paket Photobooth Gratis'),
        ('Food',        'Voucher Makanan Rp50.000'),
        ('Transport',   'Diskon Transportasi 25%'),
        ('Souvenir',    'Paket Souvenir Wisata'),
        ('Adventure',   'Diskon Tur Petualangan'),
        ('Spa',         'Diskon Spa & Refleksi 20%'),
        ('Cinema',      'Beli 1 Gratis 1 Tiket Bioskop'),
        ('Museum',      'Tiket Museum Gratis'),
        ('ThemePark',   'Voucher Taman Hiburan 2×1'),
        ('Waterpark',   'Diskon Waterpark 30%'),
        ('CoffeeShop',  'Voucher Kopi Gratis'),
        ('Bakery',      'Diskon 15% Roti & Kue'),
        ('Gym',         'Uji Coba Gym Gratis 1 Minggu'),
        ('YogaStudio',  'Kelas Yoga Gratis 1×1'),
        ('ArtGallery',  'Diskon Masuk Galeri Seni'),
        ('BoatTour',    'Diskon Tur Perahu 25%'),
        ('Zoo',         'Tiket Masuk Kebun Binatang Gratis'),
        ('Aquarium',    'Diskon Aquarium 2×1'),
        ('Camping',     'Diskon Sewa Perlengkapan Berkemah'),
        ('Surfing',     'Diskon Kursus Selancar 50%'),
        ('Cooking',     'Kelas Memasak Gratis'),
        ('WineTasting', 'Voucher Wine Tasting'),
        ('CarRental',   'Diskon Sewa Mobil 20%'),
        ('BikeRental',  'Diskon Sewa Sepeda 30%'),
        ('PaddleBoard', 'Paddle Boarding Gratis 1 Jam'),
        ('PhotoPrints', 'Cetak Foto Beli 10 Gratis 1'),
        ('Bookstore',   'Voucher Toko Buku Rp75.000'),
        ('BakeryCafe',  'Diskon Kue & Kopi 20%'),
        ('IceCream',    'Es Krim Cone Gratis'),
        ('Salon',       'Diskon Salon & Perawatan Rambut 30%'),
        ('CinemaVIP',   'Diskon 2×1 Bioskop VIP'),
        ('FlowerShop',  'Diskon Bunga 25%'),
        ('GiftShop',    'Voucher Toko Oleh-oleh'),
        ('EscapeRoom',  'Diskon Escape Room 15%'),
        ('Karaoke',     'Diskon Karaoke 2 Jam'),
        ('Bowling',     'Diskon Bowling 50%'),
        ('Paintball',   'Diskon Paintball 20%')
    ]
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    code = models.CharField(max_length=10, unique=True, blank=True)
    points_required = models.PositiveIntegerField(default=2000)
    is_redeemed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(
                string.ascii_uppercase + string.digits, 
                k=8
            ))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_brand_display()} - {self.code}"