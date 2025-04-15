from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.

class CustomUser(AbstractUser):
    username_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9_.]{4,30}$',
        message='Username must be 4-30 characters long and can only contain letters, numbers, dots, and underscores.'
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        help_text='4-30 characters. Letters, numbers, dots (.), and underscores (_) only.'
    )
    
    email = models.EmailField(
        unique=True,
        validators=[EmailValidator()],
        error_messages={
            'unique': "A user with that email already exists.",
        }
    )
    points = models.PositiveIntegerField(default=0)
    registered_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if '.' in self.username and self.username.startswith('.'):
            raise ValidationError({'username': "Username cannot start with a dot."})

    def __str__(self):
        return self.username
