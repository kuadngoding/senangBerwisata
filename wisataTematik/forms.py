from django import forms
from .models import WisataTematik

class WisataTematikForm(forms.ModelForm):
    class Meta:
        model = WisataTematik
        fields = ['judul', 'deskripsi', 'gambar']
        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Judul wisata tematik'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deskripsi wisata'}),
        }
