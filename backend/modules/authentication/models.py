from django.contrib.auth.models import AbstractUser
from django.db import models

from modules.authentication.managers import CustomUserManager
from modules.core.models import BaseModel


# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    # is_active = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class ActivationToken(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    expiration_date = models.DateTimeField()
