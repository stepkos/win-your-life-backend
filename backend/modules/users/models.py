from django.db import models

from modules.core.models import BaseModel


# Create your models here.


class UserProfile(BaseModel):
    is_dark_mode = models.BooleanField(default=False)
    is_private = models.BooleanField(default=True)


class UserInfo(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    streak = models.IntegerField(default=0)


class User(BaseModel):
    email = models.EmailField(unique=True)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", blank=True, related_name="friends")
