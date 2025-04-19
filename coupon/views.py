import random
import string
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Coupon

@login_required
@transaction.atomic
def redeem_coupon(request):
    try:
        user = request.user
        if user.points < 2000:
            return JsonResponse({'error': 'Poin tidak cukup'}, status=400)
        
        code = ''.join(random.choices(
            string.ascii_uppercase + string.digits, 
            k=8
        ))
        
        coupon = Coupon.objects.create(
            user=user,
            brand=random.choice([choice[0] for choice in Coupon.BRAND_CHOICES]),
            code=code,
            points_required=2000,
            is_redeemed=True
        )
        
        user.points -= 2000
        user.save(update_fields=['points'])
        
        return JsonResponse({
            'success': True,
            'code': coupon.code,
            'brand': coupon.get_brand_display(),
            'new_points': user.points,
            'created_at': coupon.created_at.strftime("%d %b %Y")
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)