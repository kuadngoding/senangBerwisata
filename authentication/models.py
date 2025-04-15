from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    points = models.PositiveIntegerField(default=0)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
