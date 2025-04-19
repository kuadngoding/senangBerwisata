from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
import json

from .models import Review
from place.models import Place

@require_http_methods(["GET"])
def get_reviews(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    reviews = place.reviews.select_related('user').order_by('-created_at')
    data = [{
        'id': r.id,
        'user': r.user.username,
        'rating': r.rating,
        'comment': r.comment,
        'created_at': r.created_at.strftime('%Y-%m-%d %H:%M'),
    } for r in reviews]
    return JsonResponse({'reviews': data})


@csrf_exempt
@require_http_methods(["POST"])
@login_required(login_url='/auth/login')
def add_review(request, place_id):
    try:
        payload = json.loads(request.body)
        place = get_object_or_404(Place, pk=place_id)

        review = Review.objects.create(
            user=request.user,
            place=place,
            rating=payload.get('rating'),
            comment=payload.get('comment')
        )
        request.user.refresh_from_db(fields=['points'])

        return JsonResponse({
            'message': 'Review created successfully',
            'review': {
                'id': review.id,
                'user': review.user.username,
                'rating': review.rating,
                'comment': review.comment,
                'created_at': review.created_at.strftime('%Y-%m-%d %H:%M'),
            },
            'points': request.user.points,
        }, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
@login_required(login_url='/auth/login')
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    data = json.loads(request.body)
    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    review.save()
    return JsonResponse({'message': 'Review updated successfully'})


@csrf_exempt
@require_http_methods(["DELETE"])
@login_required(login_url='/auth/login')
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return JsonResponse({'message': 'Review deleted successfully'})