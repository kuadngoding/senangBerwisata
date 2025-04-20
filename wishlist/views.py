from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from place.models import Place
from django.http import JsonResponse

@login_required
def toggle_wishlist(request, place_id):
    if request.method == "POST":
        place = get_object_or_404(Place, pk=place_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, place=place)
        if not created:
            wishlist_item.delete()
            status = 'removed'
        else:
            status = 'added'
        return JsonResponse({'status': status})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def wishlist_view(request):
    wishlist_places = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_places': wishlist_places})
