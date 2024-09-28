from django.contrib.auth.models import AbstractUser
from django.db import models

from modules.authentication.managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


