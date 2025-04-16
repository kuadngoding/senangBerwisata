from django.urls import path
from . import views

urlpatterns = [
    path('redeem_coupon/<int:coupon_id>/', views.redeem_coupon, name='redeem_coupon'),
]
