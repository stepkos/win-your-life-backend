from django.db import models

from modules.core.models import BaseModel


# Create your models here.


class UserProfile(BaseModel):
    is_dark_mode = models.BooleanField(default = False)
    is_private = models.BooleanField(default = True)


class User(BaseModel):
    email = models.EmailField(unique = True)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", blank = True, related_name="friends")


