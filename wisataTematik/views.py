from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WisataTematik
from .forms import WisataTematikForm

# Create your views here.

@login_required
def tambah_rute_wisata(request):
    if request.method == 'POST':
        form = WisataTematikForm(request.POST, request.FILES)
        if form.is_valid():
            rute = form.save(commit=False)
            rute.dibuat_oleh = request.user
            rute.save()
            request.user.points += 10
            request.user.save()
            return redirect('place_list')
        else:
            print(form.errors)
    else:
        form = WisataTematikForm()
    return render(request, 'tambah_rute.html', {'form': form})

def detail_rute_wisata(request, pk):
    rute = get_object_or_404(WisataTematik, pk=pk)
    return render(request, 'detail_rute.html', {'rute': rute})
