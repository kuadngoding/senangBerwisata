from django.urls import path
from .views import redeem_coupon

app_name = 'coupon'

urlpatterns = [
    path('redeem/', redeem_coupon, name='redeem'),
]