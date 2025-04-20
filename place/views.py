# place/views.py

from django.shortcuts import render, get_object_or_404
from .models import Place
from wisataTematik.models import WisataTematik
from wishlist.models import Wishlist 

def place_list(request):
    """View untuk menampilkan semua tempat wisata di homepage"""
    places = Place.objects.all()
    tematik_list = WisataTematik.objects.all().order_by('-tanggal_dibuat')

    wishlist_place_ids = []
    if request.user.is_authenticated:
        wishlist_place_ids = Wishlist.objects.filter(user=request.user).values_list('place_id', flat=True)

    return render(request, 'place_list.html', {'places': places, 'tematik_list': tematik_list, 'wishlist_place_ids': wishlist_place_ids})

def place_detail(request, pk):
    """View untuk menampilkan detail dari satu tempat wisata"""
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'place_detail.html', {'place': place})
