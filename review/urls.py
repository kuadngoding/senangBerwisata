from django.urls import path
from . import views

urlpatterns = [
    path('place/<int:place_id>/', views.get_reviews, name='get_reviews'),
    path('place/<int:place_id>/add/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/', views.update_review, name='edit_review'),
]
