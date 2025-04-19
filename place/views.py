# place/views.py

from django.shortcuts import render, get_object_or_404
from .models import Place
from wisataTematik.models import WisataTematik

def place_list(request):
    """View untuk menampilkan semua tempat wisata di homepage"""
    places = Place.objects.all()
    tematik_list = WisataTematik.objects.all().order_by('-tanggal_dibuat')
    return render(request, 'place_list.html', {'places': places, 'tematik_list': tematik_list})

def place_detail(request, pk):
    """View untuk menampilkan detail dari satu tempat wisata"""
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'place_detail.html', {'place': place})
