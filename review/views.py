import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ReviewForm
from .models import Review
from place.models import Place
from django.utils import timezone


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
        'updated_at': r.updated_at.strftime('%Y-%m-%d %H:%M') if r.updated_at else None,
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
@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.updated_at = timezone.now()
            updated_review.save()
            return redirect('place_detail', pk=review.place.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})