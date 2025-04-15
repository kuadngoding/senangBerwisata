from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        validators=[RegexValidator(
            regex=r'^[a-zA-Z0-9_.]{4,30}$',
            message='4-30 characters. Letters, numbers, dots (.), and underscores (_) only.'
        )],
        widget=forms.TextInput(attrs={'pattern': '[a-zA-Z0-9_.]{4,30}'})
    )
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        validators=[validate_password],  # Django's built-in password validator
        help_text="Your password must meet the complexity requirements."
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.startswith('.'):
            raise ValidationError("Username cannot start with a dot.")
        return username