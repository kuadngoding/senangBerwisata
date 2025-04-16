from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Coupon
from django.http import Http404

@login_required
def profile_view(request):
    user_profile = request.user.profile
    coupons = Coupon.objects.filter(redeemed_by=None)
    return render(request, 'authentication/templates/profile.html', {
        'user_profile': user_profile,
        'coupons': coupons
    })

@login_required
def redeem_coupon(request, coupon_id):
    coupon = get_object_or_404(Coupon, id=coupon_id)
    if coupon.redeem(request.user):
        messages.success(request, 'Kupon berhasil ditukar')
    else:
        messages.error(request, 'Poin tidak cukup untuk ditukarkan')
    return redirect('profile')