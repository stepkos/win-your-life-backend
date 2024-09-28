from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ClientInfo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
