from django.db import models


# Create your models here.


class UserProfile(models.Model):
    id = models.UUIDField(primary_key = True)
    is_dark_mode = models.BooleanField(default = False)
    is_private = models.BooleanField(default = True)


class User(models.Model):
    id = models.UUIDField(primary_key = True)
    email = models.EmailField(unique = True)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", blank = True, related_name="friends")


