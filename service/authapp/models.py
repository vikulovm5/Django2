from django.db import models
from uuid import uuid4

# Create your models here.


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4())
    login = models.CharField(unique=True, max_length=16)
    password = models.CharField(max_length=32)

