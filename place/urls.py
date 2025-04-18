from django.urls import path
from .views import place_detail, place_list

urlpatterns = [
    path('', place_list, name='place_list'),
    path('<int:pk>/', place_detail, name='place_detail'),
]
