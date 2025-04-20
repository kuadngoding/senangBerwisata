from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist_view, name='wishlist'),
    path('toggle/<int:place_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/delete/<int:place_id>/', views.delete_wishlist, name='delete_wishlist'),

]
