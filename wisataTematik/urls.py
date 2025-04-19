from django.urls import path
from .views import tambah_rute_wisata, detail_rute_wisata, edit_rute_wisata

urlpatterns = [
    path('tambah/', tambah_rute_wisata, name='tambah_rute'),
    path('<int:pk>/', detail_rute_wisata, name='detail_rute'),
    path('<int:pk>/edit/', edit_rute_wisata, name='edit_rute'),
]